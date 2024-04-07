from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect,render
from django.conf import settings
from . import forms

# Create your views here.

# creation de compte
def signup_page(request):
    form = forms.SignUpForm()
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request,'authentication/signup.html',context={'form':form})
