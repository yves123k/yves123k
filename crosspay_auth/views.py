from django.shortcuts import render , redirect
from django.contrib.auth import  authenticate,logout,login
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import View
from .models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
# from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from crosspay_system_files import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from .forms import UpdateUserProfile,Signup
from .tokens import generate_token


def signup(request):
    signup_form =  Signup
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
    
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! \nPlease try some other username.")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
        
        if len(username)>8:
            messages.error(request, "Username must be under 8 charcters!!")
          
        if password != password2:
            messages.error(request, "Passwords didn't matched!!")
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
          
            user = User.objects.create_user(
                    first_name = first_name,
                    last_name = last_name,
                    username = username, 
                    email = email, 
                    password = password,  
                )
            user.is_active = False    
            user.save()
            messages.success(request, "Your Account has been created succesfully!! \nPlease check your email to confirm your email \naddress in order to activate your account.")

            # Welcome Email
            subject = "Crosspay confirm email!!"
            message = "Hello " + user.first_name + "!! \n" + "Welcome to Crosspay!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nYves kouame" 
            from_email = settings.EMAIL_HOST_USER
            to_list = [user.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

            current_site = get_current_site(request)
            email_subject = "Confirm your Email @ Good - Crosspay Login!!"
            message2 = render_to_string('accounts/email_confirmation.html',{
                
                'name': user.first_name,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': generate_token.make_token(user)
            })
            email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [user.email],
            )
            email.fail_silently = True
            email.send()
            
            return redirect('login')
        else:
            signup_form =  Signup()        

    return render(request , 'accounts/signup.html' ,{"signup_form":signup_form})


def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        if user.is_active:
            return redirect('not_found')    
        
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        user = None

    if user == None:
        return redirect('not_found')
    
    else:

        if user is not None and generate_token.check_token(user,token):
            user.is_active = True
            # user.profile.signup_confirmation = True
            user.save()
            login(request,user)
            messages.success(request, "Your Account has been activated!!")
            return redirect('login')

        else:
            return render(request,'activation_failed.html',locals())
        

def login_user(request):
    form_login =  UpdateUserProfile() 
    print(form_login.errors)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']  
        user = authenticate(
            username = request.POST.get("username"), 
            password = request.POST.get("password")
        )
        print(username)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect ('/home/') 
        else:
            messages.error(request,'username or password not correct')
            return redirect('login')
    else:       
        form_login =  UpdateUserProfile()     

    return render(request , 'accounts/Login.html',{'form_login':form_login})

  
def logout_view(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')


def valide_error(request):
    return render(request,'accounts/activation_failed.html') 


def not_found(request):
    return render(request,'accounts/404.html')
# class UpdateProfile(View):
#     template_name =  'front/update.html' 
#     class_form = UpdateUserProfile
    
#     def get(self , request):
#         form = self.class_form(instance=request.user)
        
#         return render(request , self.template_name , locals())
            
    
#     def post(self, request):
#         form = self.class_form(request.POST, instance=request.user)
        
#         if form.is_valid():
#             form.save()
#             return redirect("update")
#         return redirect("update")































# from http.client import HTTPResponse
# from django.contrib.auth import authenticate, login,logout
# from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
# # from django.contrib.auth.forms import UserCreationForm
# from authentification.forms import LoginForm, SignUpForm
# def signup(request):
#     form = SignUpForm(request.POST)
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print(username,password)
#         email =  request.POST.get('email')
#         user = User.objects.create_user(username=username, password=password,email=email)
#         user.save()
#         return redirect("login")
        
       

#     return render(request,"accounts/signup.html", {"form": form})    

# def login_user(request):
#     forms = LoginForm(request.POST)
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return render (request,'index.html')
#         # Redirect to a success page.
#         ...
#     else:
#         # Return an 'invalid login' error message.
        
#         ...
#     return render(request,'accounts/Login.html',{"forms":forms})





                 
# def signup(request):

#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             Username = request.POST['Username']
#             Password = request.POST['Password']
#             user = authenticate(Username=Username,Password=Password)
#             if user is None:
#                 return redirect('home') 
#             else:
#                 return render(request,'index.html')           
#     else:
#         form = SignUpForm()
#     return render(request, 'accounts/Signup.html', {'form': form})
