import operator
from functools import reduce
from django.apps import apps
from django.db.models import Q
from django.db.models.fields import CharField, TextField
from django.db.models.sql.constants import QUERY_TERMS
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def perform_query(Model, params, or_query=False):
    """ Performs a query in a model given the request
        parameters
        Args:
            Model: the model class
            params: request parameters
            or_query: if clauses are grouped by OR operands (default is False)
        Return:
            List of objects (queryset)
    """
    fields = [field.name for field in Model._meta.fields]

    sort = params.get('sort', '')
    order = params.get('order', 'asc')
    exclude_property = params.get('exclude_property', '')
    exclude_values = params.getlist('exclude_value', '')

    query_params = {key: value for key, value in params.items() if (key.split('__')[0] in str(fields)) and (key.split('__')[-1] in QUERY_TERMS)}
    if or_query:
        list_of_Q = [Q(**{key: val}) for key, val in query_params.items()]
        queryset = Model.objects.filter(reduce(operator.or_, list_of_Q))
    else:
        queryset = Model.objects.filter(**query_params)

    if exclude_property and (exclude_property in fields) and exclude_values:
        exclude_query = {}
        exclude_query[exclude_property + '__in'] = exclude_values
        queryset = queryset.exclude(**exclude_query)

    if sort:
        order_by = ''
        if order == 'desc':
            order_by += '-'
        order_by += sort
        queryset = queryset.order_by(order_by)

    return queryset

def perform_lookup_query(Model, params):
    """ Perform a query in a model to lookup the occurrence of
        the given argument in all model fields
        Args:
            Model: the model class
            params: request parameters
            query: value to lookup
        Return:
            List of objects (queryset)
    """
    fields = [field for field in Model._meta.fields if not field.remote_field]
    query = params.get('q', '')

    new_params = params.copy()

    for field in fields:
        if type(field) in [CharField, TextField]:
            # Unaccent is for postgres databases (Remove if you use others databases)
            new_params.update({field.name + '__unaccent__icontains': query})
        else:
            new_params.update({field.name + '__icontains': query})

    print(new_params)

    return perform_query(Model, params=new_params, or_query=True)

def paginate_list(instance_list, params):
    """ Paginate a list of objects
        Args:
            instance_list: list of objects to paginate
            params: request parameters
            instances_per_page: number of objects per page
        Return:
            List of objects paginated
    """
    # Prepare paginator
    items_per_page = params.get('items_per_page', '50')
    paginator = Paginator(instance_list, items_per_page)
    page = params.get('page', 1)

    # Paginate queryset
    try:
        paginated_list = paginator.page(page)
    except PageNotAnInteger:
        paginated_list = paginator.page(1)
    except EmptyPage:
        paginated_list = paginator.page(paginator.num_pages)

    return paginated_list
