from django import template

register = template.Library()

@register.inclusion_tag('tags/sortable_column.html')
def sortable_column(property, title):
    context = {
        'property': property,
        'title': title, 
    }
    return context
