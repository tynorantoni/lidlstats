from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *




class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class ImageUpload(forms.Form):

    file=forms.ImageField(label="dodaj plik .jpg, .jpeg lub .png", required=True)
