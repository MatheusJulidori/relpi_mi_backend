from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from relpi_mi_back import settings
from relpi_miAPP.forms import RegisterForm


# Create your views here.
def index(request):
    return render(request, 'main_pages/index.html')

def contact(request):
    return render(request, 'main_pages/contact.html')

def team(request):
    return render(request, 'main_pages/team.html')

#def log(request):
   # return render(request, 'login.html')

def register(request):
    template_name = 'Registration/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')

    else :
        form = RegisterForm()
    context = {'form': form }
    return render(request, template_name, context)
