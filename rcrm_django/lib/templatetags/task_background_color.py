from django import template
from crm.models import Priority, Task


register = template.Library()


@register.simple_tag
def gen_task_background_color(task_id):
    """
    Return html background for task.
    """

    if Task.objects.get(id=task_id).closed_date:
        return "#ffffff"

    prio_weight = Task.objects.get(id=task_id).task_prio.weight

    html_background = "#cce5ff"

    if prio_weight > 24:
        html_background = "#339933"

    if prio_weight > 39:
        html_background = "#cc3300"

    return html_background
