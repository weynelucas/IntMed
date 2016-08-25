from django.shortcuts import render
from .models import Medicine
from TreatCare.utils import query_service
import math
# Create your views here.
def list(request):
    params = request.GET.copy()
    q = params.get('q', '')
    items_per_page = params.get('items_per_page', '50')
    objects = query_service.perform_lookup_query(app_label='medicine', model_name='Medicine', params=params, query=q)
    objects = query_service.paginate_list(objects, params, items_per_page)

    context = {
        'objects': objects,
        'objects_total': objects.paginator.count,
        'query': params,
        'items_per_page': items_per_page,
        'start_index': objects.start_index,
        'end_index': objects.end_index,
    }
    return render(request, 'medicine/list.html', context)
