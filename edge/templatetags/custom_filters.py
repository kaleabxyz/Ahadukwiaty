# custom_filters.py
from django import template

register = template.Library()
num = 0

@register.filter(name='calculate_id')
def calculate_id(index):
    global num
    num = num + 1
    if num < 6:
        return index * 10 + num
    else:
        num = 1
        return index * 10 + num