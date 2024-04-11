from django.contrib import admin
from patient.models import Examen_medical,Rapport_medical,Hospitalisation

# Register your models here.
class ExamenAdmin(admin.ModelAdmin):
    list_display = ('id','patient','type_rapport','date_creation')

class RapportAdmin(admin.ModelAdmin):
    list_display = ('id','motif_consultation','traitement_prescrit','recommandation','medecin','date_consultation','date_modification')

class HospitalisationAdmin(admin.ModelAdmin):
    list_display = ('patient','medecin','motif','numero_de_chambre','date_hospitalisation','actif')

admin.site.register(Examen_medical,ExamenAdmin)
admin.site.register(Rapport_medical,RapportAdmin)
admin.site.register(Hospitalisation,HospitalisationAdmin)