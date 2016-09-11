from .report.generator import ReportGenerator
from .report.writer import wrap_word_cell
from reportlab.lib.units import mm
from django.utils.translation import ugettext as _


def generate_checker_report(checker):
    report = ReportGenerator()

    selected_drugs_table = {
        'table': 'history',
        'objects': checker['selectedDrugs'],
        'labels': [_('Selected drugs')],
        'row_formatter': lambda obj: [
            obj['name']
        ]
    }

    interactions_table = {
        'table': 'history',
        'objects': checker['interactions'],
        'labels': [_('Drugs'), _('Interaction'), _('Evidence'), _('Action')],
        'row_formatter': lambda obj: [
            obj['startNode'] + "\n" + obj['endNode'],
            _(format_interaction_type(obj['type'])),
            _(obj['evidence']),
            _(obj['action'])
        ]
    }

    explanation_table = {
        'table': 'history',
        'objects': checker['interactions'],
        'labels': [_('Drugs'), _('Explanation')],
        'row_formatter': lambda obj: [
            obj['startNode'] + "\n" + obj['endNode'],
            wrap_word_cell(_(obj['explanation']))
        ],
        'colWidths': [None, 75*mm],
    }

    return report.generatePdfReport(selected_drugs_table, interactions_table, explanation_table)


def format_interaction_type (int_type):
    return ' '.join(int_type.split('INTERACTION')[0].split('_')).lower().capitalize().strip()
