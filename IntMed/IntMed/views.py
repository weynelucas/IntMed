from .utils import query_service
from .decorators import ajax_required
from django.apps import apps
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.generic.edit import FormView
from django.forms.models import model_to_dict
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

class ListView(View):
    template = "list.html"
    enable_create = True

    def get(self, request):
        # Manage params of request
        params = request.GET.copy()
        q = params.get('q', '')
        items_per_page = params.get('items_per_page', '50')

        # Perform query
        objects = query_service.perform_lookup_query(app_label=self.app_label, model_name=self.model_name, params=params, query=q)

        # Return JSON if request comes from AJAX
        if request.is_ajax():
            return JsonResponse(list(objects.values()), safe=False)

        # Pagination
        objects = query_service.paginate_list(objects, params, items_per_page)

        # Pack fields and labels
        if len(self.fields) == len(self.labels):
            self.fields_tuple = zip(self.fields, self.labels)

        # Context
        context = {
            'title': self.title,
            'query': params,
            'items_per_page': items_per_page,
            'objects': objects,
            'objects_total': objects.paginator.count,
            'start_index': objects.start_index,
            'end_index': objects.end_index,
            'fields': self.fields,
            'fields_tuple': self.fields_tuple,
            'enable_create': self.enable_create,
        }

        return render(request, self.template, context)

    class Meta:
        abstract = True

@method_decorator(ajax_required, name='dispatch')
class ModalCreateFormView(FormView):
    template_name = "modal_form.html"
    subtitle = _("Complete the form bellow")
    main_property = "name"

    def get_context_data(self, **kwargs):
        context = super(ModalCreateFormView, self).get_context_data(**kwargs)
        context.update({
            'title': self.title,
            'subtitle': self.subtitle,
        })
        return context

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=404)

    def form_valid(self, form):
        form.save()

        model_verbose_name = form.instance.__class__._meta.verbose_name.title().capitalize()
        instance_dict = model_to_dict(form.instance)
        success_context = {
            'message': _(
                "%(model_name)s %(main_property_value)s successfully added."
            ) % {
                'model_name': model_verbose_name,
                'main_property_value': instance_dict.get(self.main_property, ''),
            },
            'instance': instance_dict,
        }
        return JsonResponse(success_context)

    class Meta:
        abstract = True
