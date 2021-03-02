from django.contrib import admin
from .models import Driver, GenericUser, Sponsor, PointHist, GenericAdmin

class AdminDriver(admin.ModelAdmin):
	model = Driver
	list_display = ('username', 'first_name', 'last_name', 'phone_num', 'email', 'address', 'points')

class AdminGenericUser(admin.ModelAdmin):
	model = GenericUser
	list_display = ('username', 'type')

class AdminSponsor(admin.ModelAdmin):
	model = Sponsor
	list_display = ('username', 'first_name', 'last_name', 'email', 'sponsor_company')

class AdminAdmin(admin.ModelAdmin):
	model = GenericAdmin
	list_display = ('username', 'first_name', 'last_name', 'email')
class AdminPointHist(admin.ModelAdmin):
	model = PointHist
	list_display = ('username', 'date', 'points', 'reason')

admin.site.register(Driver, AdminDriver)
admin.site.register(GenericUser, AdminGenericUser)
admin.site.register(Sponsor, AdminSponsor)
admin.site.register(PointHist, AdminPointHist)
admin.site.register(GenericAdmin, AdminAdmin)
