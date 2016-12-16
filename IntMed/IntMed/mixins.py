from django.contrib import auth
from django.http import JsonResponse
from django.shortcuts import redirect
from django.forms.models import model_to_dict
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.contrib import messages
from IntMed.utils.request_service import get_params


class LoginFormMixin(object):
    def form_valid(self, form):
        params = get_params(self.request)

        if self.append_language_code:
            self.success_url = '/' + self.request.LANGUAGE_CODE + self.success_url

        auth.login(self.request, form.get_user())

        if self.request.is_ajax():
            return JsonResponse({'success_url': self.success_url})
        else:
            messages.success(request, 'Profile details updated.')

        return redirect(params.get('next', '') or self.success_url)


class RemoteCommandFormMixin(object):
    def form_valid(self, form):
        form.save()
        success_context = {}
        if self.return_data:
            if self.serializer_class:
                data = self.serializer_class(form.instance).data
            else:
                data = model_to_dict(form.instance)
            success_context['data'] = data
        if self.reload_page:
            messages.success(self.request, ugettext(self.success_message))
            success_context['reload'] = True
        else:
            success_context['message'] = ugettext(self.success_message),

        return JsonResponse(success_context)


class AttachRequestMixin(object):
    def get_form_kwargs(self, **kwargs):
        data = super(self.form_class, self).get_form_kwargs(**kwargs)
        data['request'] = self.request
        return data
