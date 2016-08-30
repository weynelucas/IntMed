from django.views.generic import View
from django.shortcuts import render
from TreatCare.utils import query_service

class ListView(View):
    app_label = ""
    model_name = ""
    fields = []

    def get(self, request):
        params = request.GET.copy()
        q = params.get('q', '')
        items_per_page = params.get('items_per_page', '50')
        objects = query_service.perform_lookup_query(app_label=self.app_label, model_name=self.model_name, params=params, query=q)
        objects = query_service.paginate_list(objects, params, items_per_page)

        context = {
            'objects': objects,
            'objects_total': objects.paginator.count,
            'query': params,
            'items_per_page': items_per_page,
            'start_index': objects.start_index,
            'end_index': objects.end_index,
            'fields': self.fields,
        }
        return render(request, 'list.html', context)

    class Meta:
        abstract = True
