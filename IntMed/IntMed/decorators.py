from django.http import Http404


def ajax_required(view_function):
    """ Decorator to enable valid response from view function
        only if the request is ajax
    """
    def wrap(request, *args, **kwargs):
        if request.method != 'GET' or (request.method == 'GET' and request.is_ajax()):
            return view_function(request, *args, **kwargs)
        else:
            raise Http404
    return wrap


def append_owner(view_function):

    def wrap(request, *args, **kwargs):
        request.GET.update({ 'user': request.user })
        return view_function(request, *args, **kwargs)

    return wrap
