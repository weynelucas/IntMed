from .utils import query_service
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from .decorators import ajax_required, redirect_when_authenticated
from accounts.forms import  SignUpForm, SignInForm
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required

@redirect_when_authenticated
def home(request):
    context = {
        'signin_form': SignInForm,
        'signup_form': SignUpForm,
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
            'items_per_page': self.params.get('items_per_page', '50'),
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
    subtitle = _("Complete the form bellow")
    url = "create/"
    form_id = "modal_form"
    template_name = "modal_form.html"
    has_owner = False
    validate_form = True
    attach_request = False
    append_language_code = False

    def get_initial(self):
        initial = super(AjaxFormView, self).get_initial()
        if self.has_owner:
            initial['owner'] = self.request.user.id

        return initial

    def get_form_kwargs(self, **kwargs):
        data = super(AjaxFormView, self).get_form_kwargs(**kwargs)
        if self.attach_request:
            data['request'] = self.request
        return data

    def get_context_data(self, **kwargs):
        if self.append_language_code:
            url = '/' + self.request.LANGUAGE_CODE + self.url
        else:
            url = self.url

        context = super(AjaxFormView, self).get_context_data(**kwargs)
        context.update({
            'url': url,
            'title': self.title,
            'subtitle': self.subtitle,
            'form_id': self.form_id,
            'validate_form': self.validate_form,
        })
        return context

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=404)

    class Meta:
        abstract = True
