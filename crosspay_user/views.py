from django.shortcuts import render,redirect
from django.db import models
from django.conf import settings
from crosspay_auth.forms import UpdateUserProfile
from crosspay_auth.models import RepeatField
from .forms import ad_user
# Create your views here.

# class Competence(RepeatField):
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.SET_NULL,
#         null=True,
#         related_name="competence_user",
#     )
#     name = models.CharField(max_length=150)
#     description = models.TextField()


def profile(request):
    form_up = UpdateUserProfile()
    
    
    return render(request, 'profile/profil.html',{'form_up':form_up})

def add_ad(request):
    # form_ad = ad_user
    if request.method == "POST":
        print("ok")
        form_ad = ad_user(request.POST,request.FILES)
        print(request.FILES)
    # check whether it's valid:
        if form_ad.is_valid():
            form_ad.save() 
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('home/')
            
    else:
        form_ad = ad_user()

    return render(request, 'profile/post_your_ad.html',{'form_ad':form_ad})   

     