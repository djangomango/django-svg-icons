# Django-Svg-Icons

A lightweight Django package providing an icon-focused SVG template tag bundled with pre-packaged icons from Iconify (Heroicons, Material Design Icons, and more).

---

## Installation

```bash
pip install git+https://github.com/djangomango/django-svg-icons.git@0.1.0
```

Or add to your `requirements.txt`:

```txt
git+https://github.com/djangomango/django-svg-icons.git@0.1.0
```

Add `django_svg_icons` to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    "django_svg_icons",
    ...
]
```

---

## Usage

Load the `svg_icon` template tag library and render SVG icons directly:

```html
{% load svg_icon %}

<!-- Render Material Design icon -->
{% svg_icon "mdi" "check" fill_color="green" size=20 extra_class="mr-2" %}

<!-- Render Heroicon -->
{% svg_icon "heroicons" "magnifying-glass" size=24 extra_class="text-gray-500" %}
```

---

## Icon Updates (Optional)

To rebuild or update bundled icon sets from upstream Iconify:

```bash
git subtree add --prefix=iconify https://github.com/iconify/icon-sets.git master --squash
python extract_iconify_icons.py
```

---

## License & Credits

- Licensed under the **GNU Lesser General Public License v3 (LGPLv3)**.
- Pre-packaged SVG icon sets provided by [Iconify](https://github.com/iconify).