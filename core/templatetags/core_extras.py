from django import template

register = template.Library()


@register.filter
def allowed(value):
    return 'allowed' if value > 13 else 'blocked'


@register.filter
def bizzfuzz(value):
    if value % 3 == 0 or value % 5 == 0:
        result = ''
        if value % 3 == 0:
            result += 'Bizz'
        if value % 5 == 0:
            result += 'Fuzz'

        return result

    return value
