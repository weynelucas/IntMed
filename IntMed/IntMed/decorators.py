from django.http import Http404
from django.shortcuts import redirect
from django.conf import settings


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

def redirect_when_authenticated(view_function):
    """ Decorator to redirect if user is authenticated
    """
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(settings.AUTH_REDIRECT_URL)

        return view_function(request, *args, **kwargs)

    return wrap
