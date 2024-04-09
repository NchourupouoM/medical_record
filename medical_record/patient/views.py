from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authentication.models import User
from .models import Examen_medical,Rapport_medical

from . import forms

# Create your views here.
#========================== page d'acceuil =============================
@login_required
def home(request):
    return render(request,'patient/homepage.html')

#=========================== liste des patient ==========================
# liste des patients
def patient_list(request):
    patients = User.objects.filter(groups__name='patient')
    return render(request,'patient/patient_list.html',{"patients":patients})

#============================ Dossier medical ============================
def dossier_medical(request,id):
    user = User.objects.get(id=id)
    dossiers = Examen_medical.objects.filter(patient=user)
    return render(request,'patient/examen_medical.html',{"dossiers":dossiers})

#============================ rapport medical ============================
def rapport_medical(request,id):
    examen = Examen_medical.objects.get(id=id)
    rapports = Rapport_medical.objects.filter(examen_medical=examen)
    return render(request,'patient/rapport_medical.html',{"rapports":rapports})

# ============================= creer rapport medical =======================
def creer_rapport_medical(request,id):
    examen = Examen_medical.objects.get(id=id)
    form = forms.RapportmedicalForm()
    if request.method == 'POST':
        form = forms.RapportmedicalForm(request.POST)
        if form.is_valid():
            rapport = form.save(commit=False)
            rapport.medecin = request.user
            rapport.examen_medical = examen
            rapport.save()
            return redirect('patient_list')
    return render(request,'patient/rapport_medical_form.html',{"form":form})

#============================ creation dossier medical ====================
def create_dossier_medical(request, id):
    user = User.objects.get(id=id)
    form = forms.DossierMedicalForm(initial={'patient': user})

    if request.method == 'POST':
        form = forms.DossierMedicalForm(request.POST)
        if form.is_valid():
            dossier = form.save(commit=False)  # Ne pas sauvegarder directement
            dossier.patient = user  # Assigner le patient manuellement
            dossier.save()  # Sauvegarder l'instance avec le champ patient
            return redirect('patient_list')
    return render(request, 'patient/form_examen_medical.html', {"form": form})
