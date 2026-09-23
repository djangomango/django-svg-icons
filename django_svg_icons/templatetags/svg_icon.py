from typing import Any
from xml.etree.ElementTree import Element, ParseError, fromstring, tostring

from django import template
from django.utils.safestring import SafeString, mark_safe

from ..helpers import load_icon_body

register = template.Library()


@register.simple_tag
def svg_icon(
    icon_type: str,
    icon_name: str,
    view_box: str = "0 0 24 24",
    width: int | str = 20,
    height: int | str = 20,
    x: int | str = 0,
    y: int | str = 0,
    preserve_aspect_ratio: str = "xMidYMid meet",
    xmlns: str = "http://www.w3.org/2000/svg",
    extra_class: str | None = None,
    extra_style: str | None = None,
    **kwargs: Any,
) -> SafeString:
    """Render an SVG icon with customizable dimensions, classes, and styles."""
    svg_root = Element(
        "svg",
        {
            "viewBox": view_box,
            "width": str(width),
            "height": str(height),
            "x": str(x),
            "y": str(y),
            "preserveAspectRatio": preserve_aspect_ratio,
            "xmlns": xmlns,
        },
    )

    if extra_class:
        svg_root.set("class", extra_class)
    if extra_style:
        svg_root.set("style", extra_style)

    icon_body = load_icon_body(icon_type, icon_name)
    if not icon_body:
        return mark_safe(f"<!-- Icon {icon_type}/{icon_name} not found -->")

    try:
        icon_path = fromstring(icon_body)
        for key, value in kwargs.items():
            if value is not None:
                icon_path.set(key.replace("_", "-"), str(value))
        svg_root.append(icon_path)
    except ParseError:
        return mark_safe(
            f"<!-- Invalid SVG content for icon {icon_type}/{icon_name} -->"
        )

    svg = tostring(svg_root, encoding="unicode", method="xml")

    return mark_safe(svg)
