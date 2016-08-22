from django.shortcuts import render
from .models import Medicine

# Create your views here.
def list(request):
    objects = Medicine.objects.all()
    context = {
        'objects': objects,
    }
    return render(request, 'medicine/list.html', context)
