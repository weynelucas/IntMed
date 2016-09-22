from .forms import SignUpForm, SignInForm
from IntMed.views import AjaxFormView
from IntMed.mixins import LoginFormMixin
from django.utils.translation import ugettext_lazy as _


class SignInFormView(LoginFormMixin, AjaxFormView):
    form_class = SignInForm
    title = _('Sign in')
    template_name = 'accounts/signin_modal_form.html'
    url = '/accounts/login/'
    success_url = '/drug/interactions/'
    append_language_code = True
