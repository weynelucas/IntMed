from django.shortcuts import render
from .models import Disease
from TreatCare.utils import query_service
from TreatCare.views import ListView
# Create your views here.
def list(request):
    params = request.GET.copy()
    q = params.get('q', '')
    items_per_page = params.get('items_per_page', '50')
    objects = query_service.perform_lookup_query(app_label='disease', model_name='Disease', params=params, query=q)
    objects = query_service.paginate_list(objects, params, items_per_page)

    context = {
        'objects': objects,
        'objects_total': objects.paginator.count,
        'query': params,
        'items_per_page': items_per_page,
        'start_index': objects.start_index,
        'end_index': objects.end_index,
    }
    return render(request, 'disease/list.html', context)

class DiseaseListView(ListView):
    app_label = "disease"
    model_name = "Disease"
    fields = Disease._meta.fields
