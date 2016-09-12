import ast
from datetime import datetime
from django.shortcuts import render
from django.http import Http404, HttpResponse
from IntMed.views import ModalCreateFormView
from .report import generator
from .forms import DrugInteractionCheckerForm
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext

class DrugInteractionCheckerFormView(ModalCreateFormView):
    title = _('Save Drug Interaction')
    subtitle = _('Save your most searched multiple drugs interactions to check them more easily in the future.')
    success_message = 'Drug interaction successfully added'
    form_class = DrugInteractionCheckerForm
    url = '/checker/create/'
    append_language_code = True

def export(request):
    try:
        checker = ast.literal_eval(request.GET['checker'])
    except:
        raise Http404()

    filename = 'Multiple_Drugs_Interaction_Report_' + datetime.now().strftime('%Y_%m_%d__%H_%M')
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachement; filename=%(filename)s.pdf' % {'filename': filename}

    pdf = generator.generateCheckerPdfReport(checker)

    response.write(pdf)
    return response
