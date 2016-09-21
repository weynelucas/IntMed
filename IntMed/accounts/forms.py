from django import forms
from IntMed.widgets import form_control
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignUpForm(UserCreationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs=form_control), required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs=form_control), max_length=30, required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs=form_control), max_length=30, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=form_control), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=form_control), required=True)

    class Model:
        model = User
        exclude = ['email']

class SignInForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs=form_control))
    password = forms.CharField(widget=forms.PasswordInput(attrs=form_control))
