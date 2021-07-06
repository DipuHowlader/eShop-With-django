from django import forms
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

