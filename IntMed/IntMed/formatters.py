def format_interaction_type (interaction_type):
    return ' '.join(interaction_type.split('INTERACTION')[0].split('_')).lower().capitalize().strip()
