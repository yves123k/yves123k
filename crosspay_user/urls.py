from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import  add_ad



urlpatterns = [
    path('create/',add_ad,name='create'),
    
    # path( 'password_change/' ,name='password_change'),
    # path( 'password_change/done/' ,name='password_change_done'),
    # path( 'password_reset/ ,name='password_reset'),
    # path( 'password_reset/done/' ,name='password_reset_done'),
    # path( 'reset/<uidb64>/<token>/' ,name='password_reset_confirm'),
    # path( 'reset/done/' name='password_reset_complete')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)