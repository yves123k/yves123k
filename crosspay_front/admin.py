from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Footer_Contact_info)
class Footer_contact(admin.ModelAdmin):
    list_display = ("address","number","email",)

@admin.register(Footer_Link)
class Footer_Link(admin.ModelAdmin):
    list_display = ("link",)

@admin.register(Footer_Lastest_blog)
class Footer_blog(admin.ModelAdmin):
    list_display = ("blog",)

@admin.register(Footer_About)
class Footer_About(admin.ModelAdmin):
    list_display = ("text",)

@admin.register(Copyright)
class Copyright(admin.ModelAdmin):
    list_display = ("text",)

class Copyrignt_icon(admin.ModelAdmin):
    list_display = ("icon",)

@admin.register(Slider)
class Slider(admin.ModelAdmin):
    list_display = ("titre","image",)