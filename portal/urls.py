from django.urls import path
from . import views

# list of URL's for this app
urlpatterns = [
    path('', views.portal_home, name="portal_home"),
    path('login-routing/', views.home, name='home'),
	path('register/', views.register, name='register-user'),
	path('driver_home/', views.driver_home, name='driver-home'),
    path('sponsor_home/', views.sponsor_home, name='sponsor-home'),
    path('admin/', views.GenericAdmin, name='admin-home'),
    path('admin/', views.GenericAdmin, name='admin-home'),
    path('catalog_sponsor/',views.catalog_sponsor, name='catalog-sponsor'),
    path('list_item/',views.sponsor_list, name='sponsor-list-item')
]
