from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeDoneView,PasswordChangeView

import authentication.views
import patient.views

urlpatterns = [
    path("admin/", admin.site.urls),
    # authentication urls
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
    path('signup/',authentication.views.signup_page, name='signup'),
    # patient urls
    path('home/',patient.views.home, name='home'),
    path('patient_list/',patient.views.patient_list,name='patient_list'),
    path('patient_list/<int:id>/dossier_medical/',patient.views.dossier_medical,name='dossier_medical'),
    path('patient/<int:id>/creer_dossier_medical/',patient.views.create_dossier_medical,name='creer_dossier_medical'),
    # rapport medical
    path('dossier/<int:id>/rapport_medical/',patient.views.rapport_medical,name='rapport_medical'),
    path('dossier/<int:id>/creer_rapport_medical/',patient.views.creer_rapport_medical,name='creer_rapport_medical'),
    #hospitalisation
    path('hospitalise_patient/<int:id>/',patient.views.hospitalisationform,name='hospitalise_patient'),
    path('list_patient_hospitalises/',patient.views.list_patient_hospitalise,name='list_patient_hospitalise')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
