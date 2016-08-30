from django.apps import apps
from .utils import query_service
from django.shortcuts import render
from django.views.generic import View

class ListView(View):
    title = ""
    app_label = ""
    model_name = ""
    fields = []
    labels = []

    def get(self, request):
        # Manage params of request
        params = request.GET.copy()
        q = params.get('q', '')
        items_per_page = params.get('items_per_page', '50')

        # Perform query
        objects = query_service.perform_lookup_query(app_label=self.app_label, model_name=self.model_name, params=params, query=q)
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
        }

        return render(request, 'list.html', context)

    class Meta:
        abstract = True
