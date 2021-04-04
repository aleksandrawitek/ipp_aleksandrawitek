from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from .forms import CreateUserForm

def glowna(request):
    return render(request, 'kalendarzapp/glowna.html', {})

def register(request):
    form = CreateUserForm()

    if request.method == 'POST' :
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'kalendarzapp/register.html', {'form' :form})
