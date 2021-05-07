from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.mail import send_mail
from kalendarz.settings import EMAIL_HOST_USER

# Create your views here.

@login_required(login_url='login')
def glowna(request):
    meetings = list(Meeting.objects.all())
    blocks = list(Block.objects.all())
    email = request.user.email
    return render(request, 'kalendarzapp/glowna.html', {'meetings':meetings, 'blocks': blocks, 'email': email})
    
@login_required(login_url='login')
def addnew(request):
    meetings = list(Meeting.objects.all())
    blocks = list(Block.objects.all())
    email = request.user.email
    user = request.user.username
    if request.method == 'POST' :
        if request.POST.get('day') and request.POST.get('month') and request.POST.get('year') and request.POST.get('hour_start') and request.POST.get('minute_start') and request.POST.get('hour_stop') and request.POST.get('minute_stop'):
            meeting = Meeting()
            meeting.day = request.POST.get('day')
            meeting.month = request.POST.get('month')
            meeting.year = request.POST.get('year')
            meeting.user = user
            meeting.hour_start = request.POST.get('hour_start')
            meeting.hour_stop = request.POST.get('hour_stop')
            meeting.minute_start = request.POST.get('minute_start')
            meeting.minute_stop = request.POST.get('minute_stop')
            meeting.save()
            tekst = "Cześć, " +  user + "!" + "\n" + "\n" + "Dodano nowe spotkanie - korepetycje matematyka: \n \n" + "Data: " + str(request.POST.get('day')) + "-" + str(request.POST.get('month')) + "-" + str(request.POST.get('year')) +",\n" + 'Godzina rozpoczęcia: ' + str(request.POST.get('hour_start')) +':'+ str(request.POST.get('minute_start')) + ',\n' + 'Godzina zakończenia: ' + str(request.POST.get('hour_stop')) +":"+ str(request.POST.get('minute_stop')) + ".\n \n" + "W razie pytań proszę się kontaktować pod numerem 123-456-789. \n \n" + "Pozdrawiam, \n Aleksandra Witek"
            send_mail('Potwierdzenie umówienia wizyty',
            tekst,
            EMAIL_HOST_USER, 
            [str(email)],
            fail_silently= False)
            messages.info(request, "Poprawnie zarejestrowano spotkanie")
            return render(request, 'kalendarzapp/addnew.html', {'meetings':meetings, 'blocks': blocks, 'email': email})
        else:
            messages.info(request, "Niepoprawnie uzupełniono dane")
    else:
        return render(request, 'kalendarzapp/addnew.html', {'meetings':meetings, 'blocks': blocks, 'email': email})


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



