from django import template
from django.utils.translation import get_language
from crm.models import Priority


register = template.Library()


@register.simple_tag
def get_status_title(status_id):
    """
    Returns status title in user local.
    """
    language = get_language()

    if language == "en":
        return Priority.objects.get(id=status_id).priority_en

    else:
        return Priority.objects.get(id=status_id).priority_ru
