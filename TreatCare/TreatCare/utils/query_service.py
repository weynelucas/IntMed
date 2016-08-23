from django.apps import apps

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


    if request.method == 'POST':
        params = request.POST
    else:
        params = request.GET

    sort = params.get('sort', '')
    order = params.get('order', 'asc')

    queryset = Model.objects.filter()

    if sort:
        order_by = ''
        if order == 'desc':
            order_by += '-'
        order_by += sort
        queryset = queryset.order_by(order_by)

    return queryset
