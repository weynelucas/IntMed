from django.contrib import auth
from django.http import JsonResponse
from django.shortcuts import redirect
from django.forms.models import model_to_dict
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from IntMed.utils.request_service import get_params


class LoginFormMixin(object):

    def form_valid(self, form):
        params = get_params(self.request)

        if self.append_language_code:
            self.success_url = '/' + self.request.LANGUAGE_CODE + self.success_url

        auth.login(self.request, form.get_user())

        if self.request.is_ajax():
            return JsonResponse({'success_url': self.success_url})


        return redirect(params.get('next', '') or self.success_url)


class RemoteCreateFormMixin(object):

    def form_valid(self, form):
        form.save()

        if self.serializer_class:
            data = self.serializer_class(form.instance).data
        else:
            data = model_to_dict(form.instance)

        success_context = {
            'message': ugettext(self.success_message),
            'data': data,
        }

        return JsonResponse(success_context)
