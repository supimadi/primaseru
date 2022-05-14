from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter('to_wa')
@stringfilter
def to_wa(value):
    if value.startswith("0"):
        return f"+62{value.lstrip('0')}"
    else:
        return value
