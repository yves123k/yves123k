from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from crosspay_auth.views import login_user, logout_view, not_found,signup,activate,valide_error


urlpatterns = [
    path('login/',login_user,name='login'),
    path('signup/',signup,name='signup'),
    path('logout/',logout_view,name='logout'),
    path('activate_failed/',valide_error,name='valid_error'),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('not_fount/', not_found, name='not_found'),
    # path( 'password_change/' ,name='password_change'),
    # path( 'password_change/done/' ,name='password_change_done'),
    # path( 'password_reset/ ,name='password_reset'),
    # path( 'password_reset/done/' ,name='password_reset_done'),
    # path( 'reset/<uidb64>/<token>/' ,name='password_reset_confirm'),
    # path( 'reset/done/' name='password_reset_complete')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)