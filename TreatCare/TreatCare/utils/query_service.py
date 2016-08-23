from django.apps import apps
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def perform_query(app_label, model_name, request):
    """ Performs a query in a model given the request
        parameters
        Args:
            app_label: app containing the model to perform the query
            model_name: name of model to perform the query
            request: parameters of query
        Return:
            List of objects (queryset)
    """
    Model = apps.get_model(app_label=app_label, model_name=model_name)
    fields = [field.name for field in Model._meta.fields]

    if request.method == 'POST':
        params = request.POST
    else:
        params = request.GET

    sort = params.get('sort', '')
    order = params.get('order', 'asc')

    query_params = {key: value for key, value in params.items() if key.split('__')[0] in str(fields)}
    queryset = Model.objects.filter(**query_params)

    if sort:
        order_by = ''
        if order == 'desc':
            order_by += '-'
        order_by += sort
        queryset = queryset.order_by(order_by)

    return queryset


def paginate_list(instance_list, request, instances_per_page=20):
    """ Paginate a list of objects
        Args:
            instance_list: list of objects to paginate
            request: HTTP request
            instances_per_page: number of objects per page
        Return:
            List of objects paginated
    """
    # Prepare paginator
    paginator = Paginator(instance_list, instances_per_page)
    page = request.GET.get('page', 1)

    # Paginate queryset
    try:
        paginated_list = paginator.page(page)
    except PageNotAnInteger:
        paginated_list = paginator.page(1)
    except EmptyPage:
        paginated_list = paginator.page(paginator.num_pages)

    return paginated_list
