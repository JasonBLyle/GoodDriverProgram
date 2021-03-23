from django.db import models
from PIL import Image
# from django.contrib.postgres.fields import ArrayField

# Model for the User Table - all users will be stored in here and this table will be checked on login
class GenericUser(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	type = models.CharField(max_length=15)

# Model for Driver Table - this is missing some fields, will have to decide how to fill out later
class Driver(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=30)
	phone_num = models.CharField(max_length=15)
	email = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	points = models.IntegerField(default=0)
	# ADDED
	sponsor = models.CharField(max_length=50, default = "")
	profile_photo = models.ImageField(default='default.jpg', upload_to='profile_photos')

	def save(self):
		super().save()
		image = Image.open(self.profile_photo.path)
		if image.height > 300 or image.width > 300:
			output_size = (300, 300)
			image.thumbnail(output_size)
			image.save(self.profile_photo.path)

# Changed name of admin to avoid error thrown during migration
class GenericAdmin(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

class Sponsor(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=30)
	phone_num = models.CharField(max_length=15, default = "")
	email = models.CharField(max_length=30, default = "")
	address = models.CharField(max_length=50, default = "")
	sponsor_company = models.CharField(max_length=30, default = "")

class PointHist(models.Model):
	username = models.CharField(max_length=30)
	sponsor_username = models.CharField(max_length=30)
	date = models.CharField(max_length=30)
	points = models.IntegerField(default=0)
	reason = models.CharField(max_length=300)

class Product(models.Model):
	sponsor_company = models.CharField(max_length=30, default = "")
	idNum = models.IntegerField(default=1)
	priceRaw = models.IntegerField(default=1) #Assuming we ever reach the point of point scaling per driver...