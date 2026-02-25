from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Mate:
        class Form(forms.ModelForm):
            model = User
            fields = ['username', 'password', 'confirm_password']
        

