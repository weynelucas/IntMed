from .utils import query_service
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from .decorators import ajax_required
from accounts.forms import  SignUpForm
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required

def home(request):
    context = {
        'form': SignUpForm,
    }
    return render(request, 'home.html', context)


# Generic views
@method_decorator(login_required, name='dispatch')
class ListView(View):
    template = "list.html"
    enable_create = True
    append_owner = False
    params = {}

    def configure(self):
        self.params = self.request.GET.copy()

        # Append owner field lookup
        if self.append_owner:
            self.params.update({'user__id': self.request.user.id})

        # Pack fields and labels
        if len(self.fields) == len(self.labels):
            self.fields_tuple = zip(self.fields, self.labels)

    def get(self, request):
        self.configure()

        # Perform query
        objects = query_service.perform_lookup_query(Model=self.model, params=self.params)

        # Pagination
        objects = query_service.paginate_list(objects, self.params)

        # Context
        context = {
            'title': self.title,
            'query': self.params,
            'items_per_page': str(objects.end_index() - (objects.start_index() - 1)),
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
class AjaxFormView(FormView):
    template_name = "modal_form.html"
    subtitle = _("Complete the form bellow")
    url = "create/"
    append_language_code = False
    has_owner = False

    def get_initial(self):
        initial = super(AjaxFormView, self).get_initial()
        if self.has_owner:
            initial['owner'] = self.request.user.id

        return initial

    def get_context_data(self, **kwargs):
        if self.append_language_code:
            url = '/' + self.request.LANGUAGE_CODE + self.url
        else:
            url = self.url

        context = super(AjaxFormView, self).get_context_data(**kwargs)
        context.update({
            'title': self.title,
            'subtitle': self.subtitle,
            'url': url,
        })
        return context

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=404)

    class Meta:
        abstract = True
