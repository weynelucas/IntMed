from django import template

register = template.Library()

@register.filter
def placeholder (field, placeholder):
    return attr(field, "placeholder," + str(placeholder))

@register.filter
def attr (field, args):
    attr, value = args.split(",")
    field.field.widget.attrs.update({attr: value})
    return field
