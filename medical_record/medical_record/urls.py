from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeDoneView,PasswordChangeView

import authentication.views
import patient.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",LoginView.as_view(
        template_name = 'authentication/login.html',
        redirect_authenticated_user = True),
        name='login'),
    path('logout/',authentication.views.logout_user,name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/passwordChange.html'),
        name='password_change'
        ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'),
        name='password_change_done'
        ),
    path('home/',patient.views.home, name='home'),
    path('signup/',authentication.views.signup_page, name='signup'),
    
]
