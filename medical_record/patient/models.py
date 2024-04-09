from django.db import models
from authentication.models import User
from django.conf import settings

# Create your models here.
class Examen_medical(models.Model):
    patient = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    type_rapport = models.CharField(default="",max_length=1000,verbose_name='type de rapport')
    date_creation = models.DateTimeField(auto_now_add=True)

class Rapport_medical(models.Model):
    examen_medical = models.ForeignKey(Examen_medical,null=True,on_delete=models.CASCADE)
    motif_consultation = models.CharField(null=True,max_length=1000,verbose_name='motif de la consultation')
    traitement_prescrit = models.CharField(null=True,max_length=1000,verbose_name='traitement prescrits')
    recommandation = models.CharField(max_length=2000,null=True)
    medecin = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_consultation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateField(auto_now=True)