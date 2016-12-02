from django.utils.translation import ugettext as _
from IntMed.report.writer import wrap_word_cell

def format_interaction_type (interaction_type):
    return ' '.join(interaction_type.split('INTERACTION')[0].split('_')).lower().capitalize().strip()

def format_drugs_list (drugs_list, join_char = '\n'):
    return join_char.join([drug['name'] for drug in drugs_list])

def format_interactions_found (interactions_found):
    empty_message = _('No interactions found between selected drugs')
    severitiy_types = ['UNKNOWN_SEVERITY_INTERACTION', 'SEVERE_INTERACTION', 'MODERATE_INTERACTION', 'MILD_INTERACTION', 'NOTHING_EXPECTED']
    data = []
    total = len(interactions_found)

    if total:
        for severity_type in severitiy_types:
            labels = [interaction['severity'] for interaction in interactions_found if interaction['type'] == severity_type]
            qty = len(labels)
            if qty:
                data.append(labels[0] + ': ' + str(qty))
    else:
        return wrap_word_cell(empty_message)

    return '\n'.join(data)
