from django.contrib import admin
from django.urls import path

import authentication.views
import patient.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('signup/',authentication.views.signup_page, name='signup'),
    path('',patient.views.home, name='home')
]
