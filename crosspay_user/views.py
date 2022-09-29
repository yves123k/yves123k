from django.shortcuts import render,redirect
from django.db import models
from django.conf import settings
from crosspay_auth.forms import UpdateUserProfile
from crosspay_auth.models import RepeatField, User
from .forms import ad_user
from crosspay_user.models import creat_Ad
from crosspay_user.models import User
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
    instance = request.user
    user_blog = creat_Ad.objects.filter(user=instance.pk)   
    print(instance)
    return render(request, 'profile/profil.html',{'user_blog':user_blog})

def add_ad(request):
    # form_ad = ad_user
    if request.method == "POST":
        print("ok")
        form_ad = ad_user(request.POST,request.FILES)
        print(request.FILES)
        if form_ad.is_valid():
            f = form_ad.save(commit=False) 
            f.user = request.user
            f.save()
            return redirect('property/')
            
    else:
        form_ad = ad_user()

    return render(request, 'profile/post_your_ad.html',{'form_ad':form_ad})   

def update_profile(request):
    if request.method == "POST":
        instance = request.user
        form_up = UpdateUserProfile(request.POST,request.FILES,instance)
        
    # check whether it's valid:
        # if form_up.is_valid():
        #     user_data = User.objects.update(request.POST)
        #     user_data.save()
            
        #     return redirect('/profil/') 
        # else:
        #     return form_up

    else:
        form_up = UpdateUserProfile()


    return render(request,'profile/modify_profile.html',{'form_up':form_up})     


def profile_view(request,pk):
    view_profil = User.objects.get(pk=pk)
    view_blog_user = creat_Ad.objects.filter(user=pk)
    print(view_blog_user)

    return render(request,'profile/user_profile_view.html',{'view_profil':view_profil,'view_blog_user':view_blog_user})