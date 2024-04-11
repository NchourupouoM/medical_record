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

class Hospitalisation(models.Model):
    patient = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='patient_conserne')  # Ajouter related_name
    medecin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="medecin responsable", related_name='medecin_responsable')  # Ajouter related_name
    date_hospitalisation = models.DateTimeField(auto_now_add=True)
    motif = models.CharField(null=True, max_length=1000, verbose_name="motif hospitalisation")
    numero_de_chambre = models.CharField(null=True, max_length=100, verbose_name="numero de chambre")
    actif = models.BooleanField(default=True)

class Medicament(models.Model):
    COMPRIME = 'COMPRIME'
    GELULES = 'GELULES'
    SIROP = 'SIROP'
    AUTRES = 'AUTRES'
    forme_medoc = ((COMPRIME,'comprimés'),(GELULES,'gélules'),(SIROP,'sirop'),(AUTRES,'autres'))
    nom_medicament = models.CharField(null=True,max_length=100,verbose_name="nom du medicament")
    Dosage = models.IntegerField(null=True)
    forme_pharmaceutique = models.CharField(max_length=100,null=True,choices=forme_medoc)
    Posologie = models.CharField(max_length=1000,null=True)
    dure_traitement = models.IntegerField(verbose_name="Duree du traitement en jours")

class Ordonnance(models.Model):
    patient = models.ForeignKey(User,null=True,on_delete=models.CASCADE,related_name ="patient_beneficaire")
    medecin = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="medecin_prescripteur")
    medicament_prescrits = models.ForeignKey(Medicament,null=True,on_delete=models.CASCADE,max_length=1000, verbose_name='medicaments prescrits')
    date_prescription = models.DateTimeField(auto_now_add=True,verbose_name="Date prescription")