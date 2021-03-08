from django.shortcuts import render
from django.http import HttpResponse
from users.models import Driver, PointHist
from users.models import Sponsor
from users.models import GenericAdmin
from users.models import GenericUser
from django.shortcuts import redirect
import requests
from django.contrib.auth.models import User


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
	data = {
	'points' : driver.points,
	'point_hist' : point_hist,
	'first_name' : driver.first_name,
	'last_name' : driver.last_name,
	'phone_num' : driver.phone_num,
	'address' : driver.address,
	'profile_photo' : driver.profile_photo.url,

	# ADDED
	'sponsor' : driver.sponsor

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

	data = {
		'first_name' : sponsor.first_name,
		'last_name' : sponsor.last_name,
		'phone_num' : sponsor.phone_num,
		'address' : sponsor.address,
		'email' : sponsor.email,
		# Get rid of this variable, later.
		'sponsor_company' : sponsor.sponsor_company,
		# This will access all of the drivers assigned to the sponsors.
		'my_drivers' : my_drivers
	}
	return render(request, 'portal/sponsor_home.html', data)


def admin_home(request):
	return render(request, 'admin/')

def catalog_sponsor(request):
	# Assign the sponsor user data to the user var
	user = request.user
	# Get the sponsor username
	user = request.user
	gUser = GenericUser.objects.get(username=user.username)
	userType = gUser.type
	if userType == 'Sponsor':
		sponsor = Sponsor.objects.get(username=user.username)
		#responseGetListing = requests.get('https://openapi.etsy.com/v2/shops/WarhammerMinisUS?api_key=pmewf48x56vb387qgsprzzry')
		#response = requests.get('https://openapi.etsy.com/v2/shops/CreeepyPrints/listings/active?api_key=pmewf48x56vb387qgsprzzry')
		response = requests.get('https://openapi.etsy.com/v2/shops/'+sponsor.sponsor_company+'/listings/active?api_key=pmewf48x56vb387qgsprzzry')
		parse1 = response.json()
		parse2 = parse1['results']
		parse3 = parse2[0]
		tags = "tags: "
		for x in parse3['tags']:
			tags = tags+x+", "
		data = {
			'first_name' :parse3['title'],
			'last_name' : parse3['description'],
			'phone_num' : parse3['price'] + " " + parse3['currency_code'],
			'address' : sponsor.address,
			'email' : tags,
			# Get rid of this variable, later.
			'sponsor_company' : sponsor.sponsor_company,
			# This will access all of the drivers assigned to the sponsors.
			'items':parse2
		}
		response=render(request, 'portal/catalog_sponsor.html', data)
	else:
		response = redirect('home')
	return response

def sponsor_list(request):
	# Assign the sponsor user data to the user var
	user = request.user
	# Get the sponsor username
	gUser = GenericUser.objects.get(username=user.username)
	userType = gUser.type
	if userType == 'Driver':
		response = redirect('driver-home')
	elif userType == 'Sponsor':
		sponsor = Sponsor.objects.get(username=user.username)
		try:
			my_drivers = Driver.objects.filter(sponsor=user.username)
		except Driver.DoesNotExist:
			my_drivers = None

		data = {
			'first_name' : sponsor.first_name,
			'last_name' : sponsor.last_name,
			'phone_num' : sponsor.phone_num,
			'address' : sponsor.address,
			'email' : sponsor.email,
			# Get rid of this variable, later.
			'sponsor_company' : sponsor.sponsor_company,
			# This will access all of the drivers assigned to the sponsors.
			'my_drivers' : my_drivers
		}
		response =  render(request, 'portal/sponsor_list_item.html', data)
	elif userType == 'Admin':
		response = redirect('admin-home')
	else:
		response = redirect('logout')
	return response