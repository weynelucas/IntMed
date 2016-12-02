def get_params(request):
    return getattr(request, request.method).copy()
