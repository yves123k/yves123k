from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django import forms

# Create your models here.

class RepeatField(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Nationality(RepeatField):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class Country(RepeatField):
    name = models.CharField(max_length=150)
        
    def __str__(self):
        return self.name

class User(AbstractUser):
    nationality = models.ForeignKey(
        Nationality,
        on_delete=models.SET_NULL,
        null=True,
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
    )
    photo = models.ImageField(upload_to = "Images",blank=True)
    number_phone = PhoneNumberField(region="CI")
    address = models.CharField(max_length=150,blank=True)
    description = models.TextField(max_length=500,blank=True)
    job = models.CharField(max_length=40,blank=True)
    website = models.URLField(max_length=400,blank=True)
    experience = models.CharField(max_length=400,blank=True)
    language = models.CharField(max_length=40,blank=True)


   
    sale_house = models.BooleanField(default=False)
    sell_house = models.BooleanField(default=False)
    building = models.BooleanField(default=False)
    sell_land =models.BooleanField(default=False)
    sale_land =models.BooleanField(default=False)
    #---------services------Users---------#
    
    #--------------------------------------#
    # sale_house = models.CharField(max_length=3,blank=True)
    # sell_house = models.CharField(max_length=3,blank=True)
    # building = models.CharField(max_length=3,blank=True)
    # interior = models.CharField(max_length=3,blank=True)
    # clean = models.CharField(max_length=3,blank=True)
    # maintenance= models.CharField(max_length=3,blank=True)
    # land =models.CharField(max_length=3,blank=True)
    # sale_land =models.CharField(max_length=3,blank=True)