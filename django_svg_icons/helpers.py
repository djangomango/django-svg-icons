import functools
import json
import os
from contextlib import closing
from io import BytesIO
from zipfile import ZipFile


class IconDoesNotExist(Exception):
    pass


@functools.lru_cache(maxsize=12)
def load_icon_zip(icon_type):
    icon_zip_path = f"data/{icon_type}.zip"
    icon_zip_path = os.path.join(os.path.dirname(__file__), icon_zip_path)

    if os.path.exists(icon_zip_path):
        with open(icon_zip_path, 'rb') as f:
            return f.read()

    raise FileNotFoundError(f"Zip file for icon type {icon_type} not found.")


@functools.lru_cache(maxsize=128)
def load_icon_body(icon_type, icon_name, **kwargs):
    try:
        zip_data = load_icon_zip(icon_type)
        with closing(ZipFile(BytesIO(zip_data), 'r')) as zip_file:
            try:
                with zip_file.open(f"{icon_name}.json") as zf:
                    icon_data = json.loads(zf.read().decode('utf-8'))
                    icon_body = icon_data.get('body')
                    return icon_body
            except KeyError:
                raise IconDoesNotExist(f"Icon {icon_name} does not exist in {icon_type}.")
    except FileNotFoundError as e:
        raise IconDoesNotExist(str(e))
