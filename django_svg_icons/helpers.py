import functools
import json
from contextlib import closing
from io import BytesIO
from pathlib import Path
from typing import Any
from zipfile import ZipFile


class IconDoesNotExist(Exception):
    """Raised when the requested SVG icon cannot be found."""


@functools.lru_cache(maxsize=12)
def load_icon_zip(icon_type: str) -> bytes:
    """Read binary data of requested icon type zip archive."""
    icon_zip_path = Path(__file__).resolve().parent / "data" / f"{icon_type}.zip"

    if icon_zip_path.is_file():
        with open(icon_zip_path, "rb") as f:
            return f.read()

    raise FileNotFoundError(f"Zip file for icon type {icon_type} not found.")


@functools.lru_cache(maxsize=128)
def load_icon_body(icon_type: str, icon_name: str, **kwargs: Any) -> str | None:
    """Load SVG body element from cached icon type archive."""
    try:
        zip_data = load_icon_zip(icon_type)
        with closing(ZipFile(BytesIO(zip_data), "r")) as zip_file:
            try:
                with zip_file.open(f"{icon_name}.json") as zf:
                    icon_data = json.loads(zf.read().decode("utf-8"))
                    icon_body: str | None = icon_data.get("body")
                    return icon_body
            except KeyError:
                raise IconDoesNotExist(
                    f"Icon {icon_name} does not exist in {icon_type}."
                ) from None
    except FileNotFoundError as e:
        raise IconDoesNotExist(str(e)) from e
