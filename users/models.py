from django.db import models


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


class Sponsor(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    sponsor_company = models.CharField(max_length=30)
# driver list


class Admin(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
