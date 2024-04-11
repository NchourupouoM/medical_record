from django import forms
from .models import User

from . import models

class DossierMedicalForm(forms.ModelForm):
    class Meta:
        model = models.Examen_medical
        fields =['type_rapport']

class RapportmedicalForm(forms.ModelForm):
    class Meta:
        model = models.Rapport_medical
        fields = ['motif_consultation','traitement_prescrit','recommandation']

class HospitalisationForm(forms.ModelForm):
    class Meta:
        model = models.Hospitalisation
        fields = ['patient','medecin','motif','numero_de_chambre','actif']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrer par le groupe 'Patients'
        self.fields['patient'].queryset = User.objects.filter(groups__name='patient')
        # Filtrer par le groupe 'Medecins'
        self.fields['medecin'].queryset = User.objects.filter(groups__name='medecin')

class OrdonnanceForm(forms.ModelForm):
    class Meta:
        model = models.Ordonnance
        fields = ['patient','medecin','medicament_prescrits']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrer par le groupe 'Patients'
        self.fields['patient'].queryset = User.objects.filter(groups__name='patient')
        # Filtrer par le groupe 'Medecins'
        self.fields['medecin'].queryset = User.objects.filter(groups__name='medecin')
