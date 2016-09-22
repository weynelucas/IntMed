from django.shortcuts import render
from .models import Drug
from .forms import DrugForm
from .serializers import DrugSerializer
from api.views import ApiListView, ApiDetailsView
from IntMed.views import ListView, AjaxFormView
from IntMed.mixins import RemoteCreateFormMixin
from django.utils.translation import ugettext_lazy as _

# Browsable Views
class DrugListView(ListView):
    model = Drug
    fields = ["name", "action"]
    labels = [_("Drug"), _("Action")]
    title = _("Drugs")
    enable_create = False

class DrugFormView(RemoteCreateFormMixin, AjaxFormView):
    title = _("Add Drug")
    form_class = DrugForm

def interactions(request):
    return render(request, 'drug/interactions.html')



# Api Views
class DrugApiListView(ApiListView):
    model = Drug
    serializer_class = DrugSerializer
    many = True

class DrugApiDetailsView(ApiDetailsView):
    model = Drug
    serializer_class = DrugSerializer
