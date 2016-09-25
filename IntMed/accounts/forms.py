from django import forms
from IntMed.widgets import form_control
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class SignUpForm(UserCreationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs=form_control), required=True, label=_('E-mail'))
    first_name = forms.CharField(widget=forms.TextInput(attrs=form_control), max_length=30, required=True, label=_('First name'))
    last_name = forms.CharField(widget=forms.TextInput(attrs=form_control), max_length=30, required=True, label=_('Last name'))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=form_control), required=True, label=_('Password'))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=form_control), required=True, label=_('Password confirmation'))
    accepted_terms = forms.BooleanField(required=True, label=_('IntMed terms'), help_text=_("I agree to"))

    def save(self, commit=True):
        super(SignUpForm, self).save(commit=False)
        # Save first and last names
        user = self.instance
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

    class Model:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

class SignInForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs=form_control), label=_("E-mail"))
    password = forms.CharField(widget=forms.PasswordInput(attrs=form_control), label=_("Password"))

    error_messages = {
        'invalid_login': _("E-mail or password is incorrect."),
        'inactive': _("This account is inactive."),
    }
