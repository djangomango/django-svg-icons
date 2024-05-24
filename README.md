# Django-Svg-Icons

This package provides a simple icon-focused svg template tag, with path data for many pre-packaged icons. 
The pre-packaged icons are from [Iconify](https://github.com/iconify). You can browse their available icons 
[here](https://icon-sets.iconify.design/).

### Installation

1. Pip install or add to your requirements.txt:

    ```bash
    pip install git+https://github.com/djangomango/django-svg-icons.git@main
    ```

2. Add to INSTALLED_APPS:

    ```bash
    INSTALLED_APPS = [
        ...
        'django_svg_icons',
    ]
    ```

### Usage

Load and use the template tag:

```html
{% load svg_icon %}
{% svg_icon "mdi" "check" fill_color="green" size=20 extra_class="mr-2" %}
```


### Note

To update the icon data, feel free to pull the iconify repo, and run extract_iconify_icons.py.

```bash
git subtree add --prefix=iconify https://github.com/iconify/icon-sets.git master --squash
python extract_iconify_icons.py
```