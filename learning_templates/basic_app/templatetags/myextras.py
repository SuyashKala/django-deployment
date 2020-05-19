from django import template
register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """ Replace the letter"""
    return value.replace(arg,'')

# register.filter('cut',cut)
