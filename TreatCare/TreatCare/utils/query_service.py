import operator
from functools import reduce
from django.apps import apps
from django.db.models import Q
from django.db.models.sql.constants import QUERY_TERMS
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def perform_query(app_label, model_name, params, or_query=False):
    """ Performs a query in a model given the request
        parameters
        Args:
            app_label: app containing the model to perform the query
            model_name: name of model to perform the query
            params: request parameters
            or_query: if clauses are grouped by OR operands (default is False)
        Return:
            List of objects (queryset)
    """
    Model = apps.get_model(app_label=app_label, model_name=model_name)
    fields = [field.name for field in Model._meta.fields]

    sort = params.get('sort', '')
    order = params.get('order', 'asc')

    query_params = {key: value for key, value in params.items() if (key.split('__')[0] in str(fields)) and (key.split('__')[-1] in QUERY_TERMS)}
    if or_query:
        list_of_Q = [Q(**{key: val}) for key, val in query_params.items()]
        queryset = Model.objects.filter(reduce(operator.or_, list_of_Q))
    else:
        queryset = Model.objects.filter(**query_params)

    if sort:
        order_by = ''
        if order == 'desc':
            order_by += '-'
        order_by += sort
        queryset = queryset.order_by(order_by)

    return queryset

def perform_lookup_query(app_label, model_name, params, query):
    """ Perform a query in a model to lookup the occurrence of
        the given argument in all model fields
        Args:
            app_label: app containing the model to perform the query
            model_name: name of model to perform the query
            params: request parameters
            query: value to lookup
        Return:
            List of objects (queryset)
    """
    Model = apps.get_model(app_label=app_label, model_name=model_name)
    fields = [field.name for field in Model._meta.fields]
    new_params = params.copy()
    new_params.update({field + '__icontains': query for field in fields})
    return perform_query(app_label=app_label, model_name=model_name, params=new_params, or_query=True)

def paginate_list(instance_list, params, instances_per_page=20):
    """ Paginate a list of objects
        Args:
            instance_list: list of objects to paginate
            params: request parameters
            instances_per_page: number of objects per page
        Return:
            List of objects paginated
    """
    # Prepare paginator
    paginator = Paginator(instance_list, instances_per_page)
    page = params.get('page', 1)

    # Paginate queryset
    try:
        paginated_list = paginator.page(page)
    except PageNotAnInteger:
        paginated_list = paginator.page(1)
    except EmptyPage:
        paginated_list = paginator.page(paginator.num_pages)

    return paginated_list
