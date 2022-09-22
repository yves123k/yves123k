# Register your models here.

from django.contrib import admin
from .models import Nationality,User,Country

# Register your models here.
@admin.register(User)
class User(admin.ModelAdmin):
    list_display = (
        "username" ,
        "email",
        "first_name",
        "last_name",

    )

@admin.register(Country)
class Country(admin.ModelAdmin):
    list_display = ("name",)
        
@admin.register(Nationality)
class Nationality(admin.ModelAdmin):
    list_display = ("name",)