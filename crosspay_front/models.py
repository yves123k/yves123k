from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Footer_Contact_info(models.Model):
    address = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.address

class Footer_Link(models.Model):
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.link

class Footer_Lastest_blog(models.Model):
    blog = models.CharField(max_length=200)

    def __str__(self):
        return self.blog

class Footer_About(models.Model):
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.text

class Copyright(models.Model):
    text = models.CharField(max_length=100)
    
    def __str__(self):
        return self.text

class Banner(models.Model):
    logo = models.CharField(max_length=40)

    def __str__(self):
        return self.logo

class Slider(models.Model):
    titre = models.CharField(max_length=400)
    image =models.ImageField(upload_to = 'Images')

    def __str__(self):
        return self.titre

class Copyrignt_icon(models.Model):
    icon =models.CharField(max_length=400)

    def __str__(self):
        return self.icon