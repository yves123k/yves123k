# Create your views here.
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from crosspay_user.models import creat_Ad 
from crosspay_auth.models import User
# Create your views here.

def index(request):
    return render(request,'index.html',locals())

# @login_required
def property_details(request,pk):
    details = creat_Ad.objects.get(pk=pk)
    # author = User.objects.get(pk=pk)
    
    print(request.user)
    print(details)
    return render(request,'property_details.html',locals())  

@login_required
def work(request):
    return render(request,'work.html',locals())


def contact(request):
    return render(request,'contact.html',locals())

# @login_required


def property(request):
    allhome = creat_Ad.objects.all()
    search = request.GET.get('search')
    if search == 'sale':
        allhome = allhome.filter(on_sale=True)
    if search == 'rent':
        allhome = allhome.filter(for_rent=True)
    if search == 'all':
        allhome = creat_Ad.objects.all()            
    return render(request,'property.html',locals()) 

def welcome(request):
    return render(request,'welcome.html',locals())

def about(request):
    return render(request,'about.html',locals()) 

def blog(request):
    all_user = User.objects.all()
    return render(request,'blog.html',{'all_user':all_user})  

    