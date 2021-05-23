from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email','password1', 'password2']

class ChangePhoto(ModelForm):
    class Meta:
        model = Historie
        fields = ['profile_pic']