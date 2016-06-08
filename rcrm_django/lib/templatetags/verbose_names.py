from django import template


register = template.Library()


def uncapstring(value):
    """
    Uncapitalize letters in the string
    """
    # TODO: modify with ignoring capitalized words

    value = value.lower()
    value = value[0].upper() + value[1:]

    return value


@register.simple_tag
def get_verbose_field_name(instance, field_name):
    """
    Returns verbose_name for a field.
    """
    title = instance._meta.get_field(field_name).verbose_name.title()
    title = uncapstring(title)

    return title
