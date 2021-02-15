from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, SponsorRegistrationForm
from .models import GenericUser
from django.contrib.auth.models import User
from django.contrib.auth import login

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
