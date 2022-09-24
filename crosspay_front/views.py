# Create your views here.
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from crosspay_user.models import creat_Ad 
# Create your views here.

def index(request):
    return render(request,'index.html',locals())

# @login_required
def property_details(request,pk):
    details = creat_Ad.objects.get(pk=pk)
    return render(request,'property_details.html',locals())  

@login_required
def work(request):
    return render(request,'work.html',locals())


def contact(request):
    return render(request,'contact.html',locals())

# @login_required

from crosspay_user.models import creat_Ad
def property(request):
    allhome = creat_Ad.objects.all()
    search = request.GET.get('search')
    if search == 'sale':
        allhome = allhome.filter(on_sale=True)    
    return render(request,'property.html',locals()) 

def welcome(request):
    return render(request,'welcome.html',locals())

def about(request):
    return render(request,'about.html',locals()) 

def blog(request):
    return render(request,'blog.html',locals())    