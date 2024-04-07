from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    PATIENT = 'PATIENT'
    MEDECIN = 'MEDECIN'
    MASCULIN = 'M'
    FEMININ = 'F'

    ROLE_CHOICES_ONE = (
        (PATIENT,'patient'),
        (MEDECIN,'medecin'),
    )

    ROLE_CHOICES_TWO = (
        (MASCULIN,'M'),
        (FEMININ,'F'),
    )
    
    profile_photo = models.ImageField(verbose_name='photo de profil')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES_ONE, verbose_name='rôle')
    date_naissance = models.DateField()
    sex = models.CharField(max_length=1,choices=ROLE_CHOICES_TWO,verbose_name='sexe')
    telephone = models.IntegerField(null=True)

