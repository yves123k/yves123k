"""crosspay_system_files URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from crosspay_user.views import profile, profile_view,update_profile
from crosspay_front.views import index,welcome,property_details,work,contact,about,property,blog
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', index ,name='home'),
    path('property_details/',property_details ,name='property_details'),
    path('work/', work ,name='work'),
    path('contact/', contact ,name='contact'),
    path('property/', property ,name='property'),
    path('blog/', blog ,name='blog'),
    path('about/', about ,name='about'),
    path('welcome/', welcome ,name='welcome'),
    path('profil/', profile ,name='profil'),
    path('profile/update',update_profile,name='update_profile'),
    path('profil/user/<int:pk>/',profile_view,name='profil_view'),
    path('accounts/', include('crosspay_auth.urls')),
    path('ad/', include('crosspay_user.urls')),
    path('properties/info/<int:pk>/', property_details , name='details')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)