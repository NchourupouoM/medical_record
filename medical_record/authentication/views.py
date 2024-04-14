from django.shortcuts import render
from django.contrib.auth import login, logout
from django.shortcuts import redirect,render
from django.contrib.auth.decorators import permission_required

from django.conf import settings
from . import forms

# Create your views here.

# creation de compte
@permission_required('authentication.add_user')
def signup_page(request):
    form = forms.SignUpForm()
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request,user)
            return redirect('home')
    return render(request,'authentication/signup.html',context={'form':form})

def logout_user(request):
    logout(request)
    return redirect('login')
