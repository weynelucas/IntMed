from django import template
from urllib.parse import urlparse, urlunparse
from TreatCare.utils.url_service import remove_params, append_params

register = template.Library()

@register.inclusion_tag('tags/sortable_column.html')
def sortable_column(property, title, request):
    full_path = request.get_full_path()
    cleaned_path = remove_params(full_path, ['sort', 'order'])

    if request.method == 'POST':
        params = request.POST
    else:
        params = request.GET

    sort = params.get('sort')
    order = 'asc'
    orders = ['asc', 'desc']

    sort_icon_suffix = ''
    if sort == property:
        order =  params.get('order', 'asc')
        sort_icon_suffix = '-'  + order
        order = orders[(orders.index(order)+1)%len(orders)]

    path = append_params(cleaned_path, {'sort':property, 'order':order})

    context = {
        'property': property,
        'title': title,
        'params': params,
        'order': order,
        'sort_icon_suffix': sort_icon_suffix,
        'path': path,
    }

    return context
