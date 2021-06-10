from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm, ChangePhoto
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.mail import send_mail
from kalendarz.settings import EMAIL_HOST_USER
from datetime import date
from celery.schedules import crontab
from celery.task import periodic_task


# Create your views here.

@login_required(login_url='login')
def glowna(request):
    meetings = list(Meeting.objects.all())
    blocks = list(Block.objects.all())
    email = request.user.email
    picture = Historie.objects.filter(user=request.user)
    return render(request, 'kalendarzapp/glowna.html', {'meetings':meetings, 'blocks': blocks, 'email': email, 'picture':picture})
    
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
@periodic_task(run_every=crontab(hour=8, minute=30, day_of_week="mon-sun"))
def reminder():
    meeting = Meeting()
    meeting.day = meeting.get('day')
    meeting.month = meeting.get('month')
    meeting.year = meeting.get('year')
    meeting.user = meeting.get('user')
    meeting.hour_start = meeting.get('hour_start')
    meeting.hour_stop = meeting.get('hour_stop')
    meeting.minute_start = meeting.get('minute_start')
    meeting.minute_stop = meeting.get('minute_stop')
    current_day = int(date.today().strftime('%d'))
    current_month = int(date.today().strftime('%m'))
    current_year = int(date.today().strftime('%y'))
    email = '308968@uni.wroc.pl' #do poprawienia
    if (int(meeting.month) == current_month):
        if ((int(meeting.day) == current_day)):
            if ((int(meeting.year) == current_year)):
                tekst = "Cześć, " +  meeting.user + "!" + "\n" + "\n" + "Przypomnienie o spotkaniu - korepetycje matematyka: \n \n" + "Data: " + str(meeting.day) + "-" + str(meeting.month) + "-" + str(meeting.year) +",\n" + 'Godzina rozpoczęcia: ' + str(meeting.hour_start) +':'+ str(meeting.minute_start) + ',\n' + 'Godzina zakończenia: ' + str(meeting.hour_stop) +":"+ str(meeting.minute_stop) + ".\n \n" + "W razie pytań proszę się kontaktować pod numerem 123-456-789. \n \n" + "Pozdrawiam, \n Aleksandra Witek"
                send_mail('PPrzypomnienie o spotkaniu',
                tekst,
                EMAIL_HOST_USER, 
                [str(email)],
                fail_silently= False)



def logoutPage(request):
    logout(request)
    return redirect('login')

def profile(request):
    email = request.user.email
    user = request.user.username
    name = request.user.first_name
    lastname = request.user.last_name
    fields = get_user_model()
    profile_fields = fields.objects.all()
    meetings = Meeting.objects.filter(user=user)
    picture = Historie.objects.filter(user=user)
    form = ChangePhoto()
    if request.method == 'POST' :
        if request.POST.get('username') or request.POST.get('email') or request.POST.get('name') or request.POST.get('lastname'):
            if request.POST.get('username') != '': 
                profile_fields.update(username = request.POST.get('username'))
            if request.POST.get('email') != '': 
                profile_fields.update(email = request.POST.get('email'))
            if request.POST.get('name') != '': 
                profile_fields.update(first_name = request.POST.get('name'))
            if request.POST.get('lastname') != '': 
                profile_fields.update(last_name = request.POST.get('lastname'))
            #profile_fields.save()
            email = request.user.email
            user = request.user.username
            name = request.user.first_name
            lastname = request.user.last_name
            messages.info(request, "Poprawnie zmieniono dane")
            return render(request, 'kalendarzapp/profile.html', {'user':user, 'email': email, 'meetings':meetings, 'name':name, 'lastname':lastname, 'picture':picture, 'form':form})
        else:
            messages.info(request, "Niepoprawnie uzupełniono dane")
    else:
        return render(request, 'kalendarzapp/profile.html', {'user':user,'email': email, 'meetings':meetings, 'name':name, 'lastname':lastname, 'picture':picture, 'form':form})

    


def delete(request):
    user = request.user.username
    current_day = int(date.today().strftime('%d'))
    current_month = int(date.today().strftime('%m'))
    current_year = int(date.today().strftime('%y'))
    meetings = Meeting.objects.filter(user=user, day = current_day)
    return render(request, 'kalendarzapp/delete.html', {'user':user, 'meetings' : meetings})
