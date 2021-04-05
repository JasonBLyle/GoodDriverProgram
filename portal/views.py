from django.shortcuts import render
from django.http import HttpResponse
from users.models import Driver, PointHist
from users.models import Sponsor, Product
from users.models import GenericAdmin
from users.models import GenericUser
from .forms import SearchBar
from django.shortcuts import redirect
import requests
from django.contrib.auth.models import User
from html import unescape


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
		'user':sponsor,
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
		prodID = ''
		prodID = request.POST.get('product-chosen')
		if prodID!='' and prodID!=None:
			print('Product ID received!')
			if Product.objects.filter(sponsor_company=sponsor.sponsor_company, idNum = prodID).exists():
				newProduct = Product.objects.filter(sponsor_company=sponsor.sponsor_company, idNum = prodID).delete()
		listed_products = Product.objects.filter(sponsor_company=sponsor.sponsor_company)
		parse1 = []
		for item in listed_products:
			parse1.append(requests.get('https://openapi.etsy.com/v2/listings/'+str(item.idNum)+'?api_key=pmewf48x56vb387qgsprzzry').json()['results'][0])
		parse3 = parse1
		tags = "tags: "
		for x in parse3:
			x['title']=unescape(x['title'])
			x['description']=unescape(x['description'])
			x['image']=requests.get('https://openapi.etsy.com/v2/listings/'+str(x['listing_id'])+'/images?api_key=pmewf48x56vb387qgsprzzry').json()['results'][0]['url_170x135']
			if len(x['title'])>50:
				x['title']=x['title'][0:49]+'...'
			if len(x['description'])>250:
				x['description']=x['description'][0:249 ]+'...'
		data = {
			'sponsor_company' : sponsor.sponsor_company,
			'items':parse3
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
	print('user retrieved')
	if userType == 'Sponsor':
		sponsor = Sponsor.objects.get(username=user.username)
		search = sponsor.list_last_search
		search = request.POST.get('search')
		prodID = ''
		prodID = request.POST.get('product-chosen')
		if search!=sponsor.list_last_search and search!=None:
			sponsor.list_last_search = search
			sponsor.save()
		if prodID!='' and prodID!=None:
			if Product.objects.filter(sponsor_company=sponsor.sponsor_company, idNum = prodID).exists()==False:
				newProduct = Product.objects.create(sponsor_company=sponsor.sponsor_company, idNum=prodID, priceRaw = float(requests.get('https://openapi.etsy.com/v2/listings/'+prodID+'?api_key=pmewf48x56vb387qgsprzzry').json()['results'][0]['price']))
		#This is a failsafe in case the database isn't cooperating with older users.
		if sponsor.list_last_search == '':
			sponsor.list_last_search = 'candle'
			sponsor.save()
		response = requests.get('https://openapi.etsy.com/v2/listings/active?keywords='+sponsor.list_last_search+'&api_key=pmewf48x56vb387qgsprzzry')
		parse1 = response.json()['results']
		for x in parse1:
			x['title']=unescape(x['title'])
			x['description']=unescape(x['description'])
			x['image']=requests.get('https://openapi.etsy.com/v2/listings/'+str(x['listing_id'])+'/images?api_key=pmewf48x56vb387qgsprzzry').json()['results'][0]['url_170x135']
			if len(x['title'])>50:
				x['title']=x['title'][0:49]+'...'
			if len(x['description'])>250:
				x['description']=x['description'][0:249 ]+'...'
		data = {
			'items': parse1,
			'searchVal': sponsor.list_last_search
			}
		response=render(request, 'portal/sponsor_list_item.html', data)
	else:
		response = redirect('home')	
	return response