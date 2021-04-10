from django.shortcuts import render
from django.http import HttpResponse
from users.models import Driver, PointHist
from users.models import Sponsor
from users.models import GenericAdmin
from users.models import GenericUser
from users.models import Application
from users.models import Sponsorship
from django.shortcuts import redirect
from django.contrib.auth.models import User
# from portal.models import UserLogin

# send user to homepage
def home(request):
	user = request.user
	gUser = GenericUser.objects.get(username=user.username)
	userType = gUser.type
	if userType == 'Driver':
		response = redirect('driver-home')
	elif userType == 'Sponsor':
		response = redirect('sponsor-home')
	elif userType == 'Admin':
		response = redirect('admin-home')
	else:
		response = redirect('logout')
	# # log login attempt
	# login_attempt = UserLogin(
	# 	username = user.username,
	# 	date= "Today",
	# 	success = "true"
	# )
	# login_attempt.save()
	return response
	#return render(request, 'portal/home.html')

def portal_home(request):
	return render(request, 'portal/home.html')

def register(request):
	return render(request, 'portal/register.html')

def driver_home(request):
	# send driver info to page
	user = request.user
	driver = Driver.objects.get(username=user.username)
	# send point history to page
	try:
		point_hist = PointHist.objects.filter(username=user.username)
	except PointHist.DoesNotExist:
		point_hist = None
	# send application data to page
	try:
		applications = Application.objects.filter(driver=user.username)
	except Application.DoesNotExist:
		applications = None
	# get sponsors and point totals
	try:
		sponsor_list = Sponsorship.objects.filter(driver=user.username)
	except Sponsorship.DoesNotExist:
		sponsor_list = None
	data = {
	'points' : driver.points,
	'point_hist' : point_hist,
	'first_name' : driver.first_name,
	'last_name' : driver.last_name,
	'phone_num' : driver.phone_num,
	'address' : driver.address,
	'profile_photo' : driver.profile_photo.url,
	'applications' : applications,
	'sponsor' : driver.sponsor,
	'sponsor_list' : sponsor_list,

	}

	return render(request, 'portal/driver_home.html', data)

def sponsor_home(request):
	# Assign the sponsor user data to the user var
	user = request.user
	# Get the sponsor username
	sponsor = Sponsor.objects.get(username=user.username)

	try:
		my_drivers = Driver.objects.filter(sponsor=user.username)
	except Driver.DoesNotExist:
		my_drivers = None
	# get applications
	try:
		applications = Application.objects.filter(sponsor=user.username)
	except Application.DoesNotExist:
		applications = None

	data = {
		'first_name' : sponsor.first_name,
		'last_name' : sponsor.last_name,
		'phone_num' : sponsor.phone_num,
		'address' : sponsor.address,
		'email' : sponsor.email,
		# Get rid of this variable, later.
		'sponsor_company' : sponsor.sponsor_company,
		# This will access all of the drivers assigned to the sponsors.
		'my_drivers' : my_drivers,
		'applications' : applications
	}
	return render(request, 'portal/sponsor_home.html', data)


def admin_home(request):
	return render(request, 'admin/')
