from django.contrib import admin
from authentication.models import User
from patient.models import Examen_medical,Rapport_medical
# Register your models here.

class ExamenAdmin(admin.ModelAdmin):
    list_display = ('id','patient','type_rapport','date_creation')

class RapportAdmin(admin.ModelAdmin):
    list_display = ('id','motif_consultation','traitement_prescrit','recommandation','medecin','date_consultation','date_modification')

class userAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','role','date_naissance','sex','telephone')

admin.site.register(Examen_medical,ExamenAdmin)
admin.site.register(Rapport_medical,RapportAdmin)
admin.site.register(User,userAdmin)