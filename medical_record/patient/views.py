from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authentication.models import User

# Create your views here.
@login_required
def home(request):
    return render(request,'patient/homepage.html')

# liste des patients
def patient_list(request):
    users = User.objects.all()
    patients = users.filter(groups__name='patient')
    return render(request,'patient/patient_list.html',{"patients":patients})