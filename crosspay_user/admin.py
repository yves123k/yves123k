from django.contrib import admin
from .models import creat_Ad
 
@admin.register(creat_Ad)
class creat_ad(admin.ModelAdmin):
    list_display = ("price",)