from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail

# class NewUserForm(UserCreationForm):    
#     email = forms.EmailField(required=True)
    
#     class Meta:   
#         model = User
#         fields = ("first_name","last_name","username","email", "password1", "password2")
        
class Signup(ModelForm):    

    
    class Meta:   
        model = User
        fields = ("first_name" , "last_name", "username", "email")
    
class UpdateUserProfile(ModelForm):    
     
    class Meta:   
        model = User
        fields = ("photo","first_name","last_name","username","email","number_phone","address","description","nationality","job","country","website","experience","language",
        "sale_house","sell_house","building","sell_land","sale_land","password")

# "sale_house","sell_house","building","interior","clean","maintenance","land","sale_land",