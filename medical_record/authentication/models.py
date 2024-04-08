from django.db import models
from django.contrib.auth.models import AbstractUser,Group

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
    date_naissance = models.DateField(null=True)
    sex = models.CharField(max_length=1,choices=ROLE_CHOICES_TWO,verbose_name='sexe')
    telephone = models.IntegerField(null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role == self.PATIENT:
            group = Group.objects.get(name='patient')
            group.user_set.add(self)
        elif self.role == self.MEDECIN:
            group = Group.objects.get(name='medecin')
            group.user_set.add(self)
