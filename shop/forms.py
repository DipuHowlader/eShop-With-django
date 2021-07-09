from django import forms
from django.contrib.auth import models
from .models import userAddress
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class customUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
       model = User
       fields = (
                'first_name',
                'last_name',
                'email',
                'password1',
                'password2',)

class customerAddress(forms.ModelForm):
    select_address = (
        ('--', '-----------'),
        ('of', 'Office'),
        ('ho', 'Home'),
        ('co', 'Commercial'),
    )

    full_name = forms.CharField(required=True)
    Mobile_number = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    zip_code = forms.CharField(max_length=6)
    town = forms.CharField(max_length=200, required=True)
    address = forms.ChoiceField(choices = select_address,required=True)

    class Meta:
        model = userAddress
        fields = (
                'full_name',
                'Mobile_number',
                'email',
                'zip_code',
                'town',
                'address',
        )