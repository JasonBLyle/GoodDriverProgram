from django.shortcuts import render
from django.http import HttpResponse
from users.models import Driver
from users.models import Admin
from users.models import Sponsor
from users.models import GenericUser
from django.shortcuts import redirect
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

def register(request):
	return render(request, 'portal/register.html')

def driver_home(request):
	# send driver info to page
	user = request.user
	driver = Driver.objects.get(username=user.username)
	data = {
	"points" : driver.points
	}
	return render(request, 'portal/driver_home.html', data)

def sponsor_home(request):
	return render(request, 'portal/sponsor_home.html')
def admin_home(request):
	return render(request, 'admin/')