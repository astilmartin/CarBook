from django.db import models


# Create your models here.

class productdb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Details = models.CharField(max_length=500, null=True, blank=True)
    Image = models.ImageField(upload_to="Product Images", null=True, blank=True)


class cardb(models.Model):
    Brand = models.CharField(max_length=100, null=True, blank=True)
    Car_Name = models.CharField(max_length=100, null=True, blank=True)
    Car_price = models.IntegerField(null=True, blank=True)
    C_Description = models.CharField(max_length=500, null=True, blank=True)
    Car_Image = models.ImageField(upload_to="Car Images", null=True, blank=True)