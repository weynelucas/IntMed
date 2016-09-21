from django.contrib import auth
from django.shortcuts import redirect
from .forms import SignUpForm, SignInForm
from IntMed.views import ModalCreateFormView
from django.utils.translation import ugettext_lazy as _


class SignInFormView(ModalCreateFormView):
    form_class = SignInForm
    title = _('Sign in')
    template_name = 'accounts/signin_modal_form.html'
    url = '/accounts/login/'
    append_language_code = True

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        return redirect('/drug/interactions')
