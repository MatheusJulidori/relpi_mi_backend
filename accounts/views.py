from django.views.generic import CreateView,FormView
from django.shortcuts import render, redirect
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.views import auth_logout

from .forms import RegisterForm


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form = form.save()
            send_mail('Relpi Mi confirmação', 'Teste de email', settings.EMAIL_HOST_USER,[form.email,settings.EMAIL_HOST_USER])
            form.save()
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def logout_request(request):
    auth_logout(request)
    #message.info(request, "Logged out successfully")
    return redirect("/accounts/login/")