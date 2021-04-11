from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, SponsorRegistrationForm, DriverUpdateFrom, SponsorUpdateForm, ApplicationForm, EditPointsForm
from .models import GenericUser, Driver, Sponsor, Application, PointHist
from django.contrib.auth.models import User
from django.contrib.auth import login
from portal.models import UserEditInfo
from datetime import date


# register new user with form input if form is valid
def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			# save user info to GenericUser table
			new_user = GenericUser(
			username = form.cleaned_data.get('username'),
			password = form.cleaned_data.get('password'),
			type = "Driver"
			)
			new_user.save()
			# save user info to Driver table
			form.save()
			# register info with user table and log them in
			user = User.objects.create_user(form.cleaned_data.get('username'), form.cleaned_data.get('email'), form.cleaned_data.get('password'))
			login(request, user)
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}')
			return redirect('driver-home')
	else:
		form = UserRegistrationForm()
	return render(request, 'users/register.html', {'form': form})

def register_sponsor(request):
	if request.method == 'POST':
		form = SponsorRegistrationForm(request.POST)
		if form.is_valid():
			# save user info to GenericUser table
			new_user = GenericUser(
			username = form.cleaned_data.get('username'),
			password = form.cleaned_data.get('password'),
			type = "Sponsor"
			)
			new_user.save()
			# save user info to Driver table
			form.save()
			# register info with user table and log them in
			user = User.objects.create_user(form.cleaned_data.get('username'), form.cleaned_data.get('email'), form.cleaned_data.get('password'))
			login(request, user)
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}')
			return redirect('sponsor-home')
	else:
		form = SponsorRegistrationForm()
	return render(request, 'users/register.html', {'form': form})

# view for editing driver profile information
def update_driver_info(request):
	if request.method == 'POST':
		driver = Driver.objects.get(username=request.user.username)
		driver_form = DriverUpdateFrom(request.POST, request.FILES, instance=driver)
		if driver_form.is_valid():
			driver_form.save()
			UserEditInfo.objects.create(username=driver.username, date = "Today", time = "")
			messages.success(request, f'Your account has been updated')
			return redirect('driver-home')
	else:
		driver = Driver.objects.get(username=request.user.username)
		driver_form = DriverUpdateFrom(instance=driver)
	context = {
		'driver_form' : driver_form
	}

	return render(request, 'users/edit_info.html', context)

def update_driver_points(request):
	print(" RUN #")
	driver = Driver.objects.get(username=request.POST.get("driver_username"))
	print(driver.username)
	print(driver.point_change_temp)
	if(driver.point_change_temp != 0):
		# Add to driver pointhist table
		# pointhist = PointHist.objects.create(driver.username, Sponsor.username, date.today().strftime("%d/%m/%Y"), driver.point_change_temp, "I havent done this yet lol")
		pointhist = PointHist.objects.create()
		pointhist.username = driver.username

		pointhist.sponsor_username = Sponsor.objects.get(username = request.user.username).username
		pointhist.date = date.today().strftime("%m/%d/%Y")
		pointhist.points = driver.point_change_temp
		pointhist.reason = "5 car pileup"
		pointhist.save()
		print("PointHistComplete")

	driver.points += driver.point_change_temp
	driver.point_change_temp = 0
	driver.save()

	driver_points_form = EditPointsForm(request.POST, instance=driver)

	if driver_points_form.is_valid():
		driver_points_form.save()
		messages.success(request, f"Your Driver's account has been updated")
		return redirect('sponsor-home')

	context = {
		'driver_points_form' : driver_points_form,
		'driver' : driver
	}
	return render(request, 'users/edit_points.html' , context)


# view for editing sponsor profile information
def update_sponsor_info(request):
	if request.method == 'POST':
		sponsor = Sponsor.objects.get(username=request.user.username)
		sponsor_form = SponsorUpdateForm(request.POST, request.FILES, instance=sponsor)
		if sponsor_form.is_valid():
			sponsor_form.save()
			messages.success(request, f'Your account has been updated')
			return redirect('sponsor-home')
	else:
		sponsor = Sponsor.objects.get(username=request.user.username)
		sponsor_form = SponsorUpdateForm(instance=Sponsor)
	context = {
		'sponsor_form' : sponsor_form
	}

	return render(request, 'users/edit_sponsor_info.html', context)

def application(request):
	if request.method == 'POST':
		application_form = ApplicationForm(request.POST)
		if application_form.is_valid():
			sponsor = application_form.cleaned_data.get('sponsor')
			sponsor_company = Sponsor.objects.get(username=sponsor)
			application = Application.objects.create(driver=request.user.username, sponsor=sponsor, sponsor_company=sponsor_company.sponsor_company, status="Pending")
			application.save()
			return redirect('driver-home')
	else:
		application_form = ApplicationForm()
	context = {
		'application_form' : application_form,
	}
	return render(request, 'users/application.html', context)
