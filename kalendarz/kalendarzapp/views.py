from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

@login_required(login_url='login')
def glowna(request):
    meetings = list(Meeting.objects.all())
    blocks = list(Block.objects.all())
    return render(request, 'kalendarzapp/glowna.html', {'meetings':meetings, 'blocks': blocks})

def register(request):
    if request.user.is_authenticated:
        return redirect('glowna')
    else:
        form = CreateUserForm()
        if request.method == 'POST' :
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Zarejestrowano użytkownika " + user)
                return redirect(loginPage)
        return render(request, 'kalendarzapp/register.html', {'form' :form})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('glowna')
    else:
        if request.method == 'POST' :
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('glowna')
                else:
                    messages.info(request, "Użytkownik lub hasło jest niepoprawne")
        return render(request, 'kalendarzapp/login.html', {})

def logoutPage(request):
    logout(request)
    return redirect('login')


