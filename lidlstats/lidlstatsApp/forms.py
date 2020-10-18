from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *




class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']




class UploadedImageForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ('title','image')
        labels = {
            'title': 'dodaj krótki opis',
            'image':'dodaj plik .jpg, .jpeg lub .png'
        }