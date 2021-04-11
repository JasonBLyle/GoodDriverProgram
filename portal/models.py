from django.db import models
from datetime import date
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from datetime import datetime

# table for logs of user login attempts
class UserLogin(models.Model):
	username = models.CharField(max_length=30)
	date = models.DateField(auto_now_add=True)
	time = models.TimeField(auto_now_add=True)
	success = models.CharField(max_length=10, default="")

class UserLogout(models.Model):
	username = models.CharField(max_length=30)
	date = models.DateField(auto_now_add=True)
	time = models.TimeField(auto_now_add=True)

class UserEditInfo(models.Model):
	username = models.CharField(max_length=30)
	date = models.DateField(auto_now_add=True)
	time = models.TimeField(auto_now_add=True)

@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
	UserLogin.objects.create(username=user.username, date = "Today", time = "", success="true")

@receiver(user_login_failed)
def user_login_failed_callback(sender, credentials, **kwargs):
	UserLogin.objects.create(username=credentials.get('username', None), date = "Today", time = "", success="false")

@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):
	UserLogout.objects.create(username=user.username, date = "Today", time = "")
