from IntMed.report.generator import ReportGenerator
from IntMed.report.writer import wrap_word_cell
from reportlab.lib.units import mm
from django.utils.translation import ugettext as _
from IntMed.formatters import format_drugs_list, format_interactions_found
from datetime import datetime

def generateCheckerPdfReport(checker, request):
    report = ReportGenerator()

    report_info_table = {
        'table': 'info',
        'title': _('General Informations'),
        'table_per_object': True,
        'objects': [{
            'user': "%(full_name)s\n%(email)s" % {'full_name': request.user.get_full_name(), 'email': request.user.email},
            'datetime': datetime.now().strftime('%d/%m/%Y %H:%M'),
            'selected_drugs': checker['selectedDrugs'],
            'interactions_found': checker['interactions'],
        }],
        'labels': [_('User'),_('Emission date'), _('Selected drugs'), _('Interactions found')],
        'formatter': lambda obj: [
            obj['user'],
            obj['datetime'],
            format_drugs_list(obj['selected_drugs']),
            format_interactions_found(obj['interactions_found']),
        ],
        'colWidths': [60*mm, 90*mm],
    }

    interactions_tables = {
        'table': 'info',
        'table_per_object': True,
        'title': _('Interaction'),
        'objects': checker['interactions'],
        'labels': [_('Drugs'), _('Severity'), _('Evidence'), _('Action'), _('Explanation')],
        'formatter': lambda obj: [
            obj['startNode'] + "\n" + obj['endNode'],
            obj['severity'],
            obj['evidence'],
            obj['action'],
            wrap_word_cell(obj['explanation'])
        ],
        'colWidths': [30*mm, 120*mm],
    }

    return report.generatePdfReport(report_info_table, interactions_tables)
