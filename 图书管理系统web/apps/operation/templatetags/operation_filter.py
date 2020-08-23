from django import template

register = template.Library()


@register.filter(name='rental_class_name')
def rental_class_name(value):
    class_dict = {
        0: 'success',
        1: 'warning',
        2: 'info',
        3: 'error',
    }
    return class_dict[value % 4]


