from xml.etree.ElementTree import Element, tostring, fromstring, ParseError

from django import template
from django.utils.safestring import mark_safe

from ..helpers import load_icon_body

register = template.Library()


@register.simple_tag
def svg_icon(
        icon_type,
        icon_name,
        view_box='0 0 24 24',
        width=20,
        height=20,
        x=0,
        y=0,
        preserve_aspect_ratio='xMidYMid meet',
        xmlns='http://www.w3.org/2000/svg',
        extra_class=None,
        extra_style=None,
        **kwargs
):
    svg_root = Element('svg', {
        'viewBox': view_box,
        'width': str(width),
        'height': str(height),
        'x': str(x),
        'y': str(y),
        'preserveAspectRatio': preserve_aspect_ratio,
        'xmlns': xmlns
    })

    if extra_class:
        svg_root.set('class', extra_class)
    if extra_style:
        svg_root.set('style', extra_style)

    icon_body = load_icon_body(icon_type, icon_name)

    try:
        icon_path = fromstring(icon_body)
        for key, value in kwargs.items():
            if value is not None:
                icon_path.set(key.replace("_", "-"), str(value))
        svg_root.append(icon_path)
    except ParseError:
        return mark_safe(f"<!-- Invalid SVG content for icon {icon_type}/{icon_name} -->")

    svg = tostring(svg_root, encoding='unicode', method='xml')

    return mark_safe(svg)
