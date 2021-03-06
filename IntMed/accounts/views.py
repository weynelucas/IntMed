from .forms import SignUpForm, SignInForm, PasswordUpdateForm
from django.shortcuts import redirect
from IntMed.views import AjaxFormView
from django.contrib import auth
from IntMed.mixins import LoginFormMixin, RemoteCommandFormMixin, AttachRequestMixin
from django.utils.translation import ugettext_lazy as _
from django.http import JsonResponse

class SignInFormView(LoginFormMixin, AjaxFormView):
    form_class = SignInForm
    title = _('Sign in')
    template_name = 'accounts/signin_modal_form.html'
    url = '/accounts/login/'
    success_url = '/interactions/'
    append_language_code = True

class PasswordUpdateFormView(RemoteCommandFormMixin, AjaxFormView):
    form_class = PasswordUpdateForm
    title = _('Change password')
    success_message = 'Your password has been changed successfully'
    url = '/accounts/change_password/'
    form_id = "change_password_form"
    attach_request = True
    return_data = False
    reload_page = True
    append_language_code = True

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])
            if new_user is not None and new_user.is_active:
                auth.login(request, new_user)
                if request.is_ajax():
                    return JsonResponse({'success_url': '/interactions/'})
                return redirect('/interactions/')
        else:
            if request.is_ajax():
                return JsonResponse(form.errors, status=404)

    return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')
