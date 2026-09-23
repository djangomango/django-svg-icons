import argparse
import json
import zipfile
from pathlib import Path
from typing import Any


def extract_iconify_icons(input_folder: str | Path, output_folder: str | Path) -> None:
    """Extract and repackage Iconify icon collections into individual zip archives."""
    in_dir = Path(input_folder)
    out_dir = Path(output_folder)
    out_dir.mkdir(parents=True, exist_ok=True)

    for json_file in in_dir.glob("*.json"):
        with open(json_file, encoding="utf-8") as f:
            icons_data: dict[str, Any] = json.load(f)

        stem = json_file.stem
        temp_dir = out_dir / stem
        temp_dir.mkdir(parents=True, exist_ok=True)

        for icon_name, icon_data in icons_data.get("icons", {}).items():
            icon_json_path = temp_dir / f"{icon_name}.json"
            with open(icon_json_path, "w", encoding="utf-8") as icon_file:
                json.dump(icon_data, icon_file, ensure_ascii=False, indent=2)

        zip_path = out_dir / f"{stem}.zip"
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for icon_path in temp_dir.iterdir():
                zipf.write(icon_path, icon_path.name)
                icon_path.unlink()

        temp_dir.rmdir()

    print("Conversion complete.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert Iconify JSON files to individual zip files."
    )
    parser.add_argument(
        "input_folder",
        nargs="?",
        default="iconify/json",
        help="Path to the folder containing the JSON files",
    )
    parser.add_argument(
        "output_folder",
        nargs="?",
        default="django_svg_icons/data",
        help="Path to the output folder for the zip files",
    )

    args = parser.parse_args()
    extract_iconify_icons(args.input_folder, args.output_folder)
