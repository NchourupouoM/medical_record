from django import forms

from . import models

class DossierMedicalForm(forms.ModelForm):
    class Meta:
        model = models.Examen_medical
        fields =['type_rapport']

class RapportmedicalForm(forms.ModelForm):
    class Meta:
        model = models.Rapport_medical
        fields = ['motif_consultation','traitement_prescrit','recommandation']