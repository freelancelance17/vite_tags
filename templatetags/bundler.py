from django import template
from django.templatetags.static import static
from django.utils.safestring import mark_safe
import os

register = template.Library()

@register.filter
def vite_js(value):

    assets_list = os.listdir(value)

    js_file = assets_list[0] if assets_list[0].endswith(".js") else assets_list[1]

    return mark_safe(f'<script type="module" crossorigin src={static(js_file)}></script>')

@register.filter
def vite_css(value):

    assets_list = os.listdir(value)

    css_file = assets_list[1] if assets_list[1].endswith(".css") else assets_list[0]

    return mark_safe(f'<link rel="stylesheet" href="{static(css_file)}">')

