
from django.db import models
from django.conf import settings
from crosspay_auth.models import User 
from ckeditor.fields import RichTextField
from crosspay_auth.models import RepeatField

class creat_Ad(RepeatField):
    user = models.ForeignKey(
        # settings.AUTH_USER_MODEL,
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="create",
        blank=True
    )
    titre = models.CharField(max_length=100,default="ND")
    image = models.ImageField(upload_to="ad",blank=True)
    price = models.FloatField(default=0,max_length=100)
    living_area = models.CharField(default=0,max_length=100)
    total_area = models.CharField(default=0,max_length=100)
    price_per_meter = models.CharField(default=0,max_length=100)
    property_type = models.CharField(max_length=100)
    year_built = models.CharField(max_length=10)
    for_rent = models.BooleanField(default=False)
    on_sale = models.BooleanField(default=False)
    address = models.TextField(max_length=40)
    more_info = models.TextField(max_length=400)
    
   
    

    ####------------principal_view_models-----------------####
    