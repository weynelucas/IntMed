import ast
from datetime import datetime
from .models import DrugInteractionChecker
from .serializers import DrugInteractionCheckerSerializer
from .report import generator
from .forms import DrugInteractionCheckerForm
from api.views import ApiListView, ApiDetailsView
from django.http import Http404, HttpResponse
from IntMed.views import AjaxFormView
from IntMed.mixins import RemoteCreateFormMixin
from api.permissions import IsOwnerOrReadOnly
from django.utils.translation import ugettext_lazy as _

# Browsable Views
class DrugInteractionCheckerFormView(RemoteCreateFormMixin, AjaxFormView):
    title = _('Save Drug Interaction')
    subtitle = _('Save your most searched multiple drugs interactions to check them more easily in the future.')
    success_message = 'Drug interaction successfully added'
    form_class = DrugInteractionCheckerForm
    url = '/checker/create/'
    append_language_code = True
    has_owner = True
    serializer_class = DrugInteractionCheckerSerializer

def export(request):
    try:
        checker = ast.literal_eval(request.GET['checker'])
    except:
        raise Http404()

    filename = 'Relatório_Interações_Medicamentosas_' + datetime.now().strftime('%Y_%m_%d__%H_%M')
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachement; filename=%(filename)s.pdf' % {'filename': filename}

    pdf = generator.generateCheckerPdfReport(checker, request)

    response.write(pdf)
    return response



# Api Views
class DrugInteractionCheckerApiListView(ApiListView):
    model = DrugInteractionChecker
    serializer_class = DrugInteractionCheckerSerializer
    many = True
    has_owner = True

class DrugInteractionCheckerApiDetailsView(ApiDetailsView):
    model = DrugInteractionChecker
    serializer_class = DrugInteractionCheckerSerializer
    delete_feedback_message = _("Drug interaction successfully removed")
