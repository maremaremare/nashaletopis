# -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def nbsp(value):
    return mark_safe(" ".join(value.split('&nbsp;')))


import random

@register.filter
def shuffle(arg):
    tmp = [i for i in arg]
    random.shuffle(tmp)
    return tmp

@register.filter
def no_dumb_chars(value):
    newval = value.replace('&nbsp;', ' ').replace('&laquo;', u'«').replace('&raquo;', u'»').replace('&ndash;', u'–')
    return newval


Stateful = {}
def do_set(parser, token):
    _, key = token.split_contents()
    nodelist = parser.parse(('endset',))
    parser.delete_first_token()  # from the example -- why?
    return SetStatefulNode(key,nodelist)

class SetStatefulNode(template.Node):
    def __init__(self, key, nodes):
        Stateful[key] = nodes
    def render(self, context):
        return ''
register.tag('set', do_set)

def do_get(parser, token):
    tag_name, key = token.split_contents()
    return GetStatefulNode(key)

class GetStatefulNode(template.Node):
    def __init__(self, key):
       self.key = key
       
    def render(self, context):
        try:
            return ''.join( [x.render(context) for x in Stateful[self.key]] )
        except:
            return ''

register.tag('get', do_get)
