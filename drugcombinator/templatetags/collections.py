from django import template


register = template.Library()


@register.filter
def get(obj, key):
    try:
        return obj[key]
    except (KeyError, IndexError):
        return None


@register.filter
def attr(obj, attr_name):
    return getattr(obj, attr_name, None)


@register.filter
def cat(obj_1, obj_2):
    return str(obj_1) + str(obj_2)


@register.filter
def humanlist(seq):
    seq = [str(x) for x in seq]
    return ', '.join(seq[:-1]) + ' et ' + seq[-1]
