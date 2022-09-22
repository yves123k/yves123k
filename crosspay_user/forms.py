from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import creat_Ad

class ad_user(forms.ModelForm):    
     
    class Meta:   
        model = creat_Ad
        fields = ('price',
                'living_area',
                'total_area',
                'property_type',
                'year_built',
                'price_per_meter',
                'for_rent',
                'on_sale',
                'year_built',
                'address',
                'more_info',
                'image'
                )
              

    