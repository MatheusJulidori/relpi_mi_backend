from django.views.generic import CreateView,FormView
from django.shortcuts import render, redirect
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.conf import settings

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