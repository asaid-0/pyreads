from django import template


register = template.Library()

@register.filter(name='quarter')
def quarter(value):
    return (0.25 * value)