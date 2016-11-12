from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    context = {
        'active': 'multiple',
    }
    return render(request, "interactions/index.html", context)

@login_required
def single(request):
    context = {
        'active': 'single',
    }
    return render(request, "interactions/single.html", context)
