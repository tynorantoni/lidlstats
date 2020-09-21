from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


# class DateInput(forms.DateInput):
#     input_type = 'date'


# class BasicDataModelForm(forms.ModelForm):
#     # Nie wiem szczerze mówiąc czy bedzie to potrzebne do czegokolwiek
#     date_of_shopping = forms.DateField(widget=DateInput())
#     product_data = forms.JSONField(widget=forms.TextInput(attrs=dict))
#     user_mail = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Twój adres Email'}))
#
#
#     class Meta:
#         model = BasicDataModel
#         fields = 'date_of_shopping', 'product_data', 'user_email'

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']