from django import forms
from IntMed.widgets import form_control
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.utils.translation import ugettext_lazy as _


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs=form_control), required=True, label=_('Username'))
    email = forms.EmailField(widget=forms.EmailInput(attrs=form_control), required=True, label=_('E-mail'))
    first_name = forms.CharField(widget=forms.TextInput(attrs=form_control), max_length=30, required=True, label=_('First name'))
    last_name = forms.CharField(widget=forms.TextInput(attrs=form_control), max_length=30, required=True, label=_('Last name'))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=form_control), required=True, label=_('Password'))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=form_control), required=True, label=_('Password confirmation'))


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError(_(u'This email is already registered.'))
        return email

    def save(self, commit=True):
        super(SignUpForm, self).save(commit=False)
        # Save not required fields
        user = self.instance
        user.email = self.clean_email()
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

    class Model:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs=form_control), label=_("E-mail"))
    password = forms.CharField(widget=forms.PasswordInput(attrs=form_control), label=_("Password"))

    error_messages = {
        'invalid_login': _("E-mail or password is incorrect."),
        'inactive': _("This account is inactive."),
    }

class PasswordUpdateForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs=form_control), required=True, label=_('Your password'))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs=form_control), required=True, label=_('New password'))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs=form_control), required=True, label=_('Confirm new password'))

    def __init__(self, **kwargs):
        self.request = kwargs.pop('request')
        super(self.__class__, self).__init__(user=self.request.user or None, data=self.request.POST or None)

    def save(self):
        super(self.__class__, self).save()
        update_session_auth_hash(self.request, self.user)

    class Meta:
        fields = ['old_password', 'new_password1', 'new_password2']
