from django.db import models

# Create your models here.

class registerdb(models.Model):
    Username = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    User_image = models.ImageField(upload_to="Profile Images", null=True, blank=True)


class bookdb(models.Model):
    Pickup = models.CharField(max_length=100,null=True,blank=True)
    Dropoff = models.CharField(max_length=100,null=True,blank=True)
    Pickup_date = models.CharField(max_length=100,null=True,blank=True)
    Dropoff_date = models.CharField(max_length=100,null=True,blank=True)
    Pickup_time = models.CharField(max_length=100,null=True,blank=True)
    Username = models.CharField(max_length=100,null=True,blank=True)
    User_Image = models.ImageField(upload_to="Booking Images", null=True, blank=True)
    Car_image = models.ImageField(upload_to="Booking Images", null=True, blank=True)
