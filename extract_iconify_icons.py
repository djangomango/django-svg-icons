import os
import json
import zipfile
import argparse


def extract_iconify_icons(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for json_file in os.listdir(input_folder):
        if json_file.endswith('.json'):
            json_path = os.path.join(input_folder, json_file)

            with open(json_path, 'r', encoding='utf-8') as f:
                icons_data = json.load(f)

            temp_dir = os.path.join(output_folder, json_file[:-5])
            os.makedirs(temp_dir, exist_ok=True)

            for icon_name, icon_data in icons_data['icons'].items():
                icon_json_path = os.path.join(temp_dir, f'{icon_name}.json')
                with open(icon_json_path, 'w', encoding='utf-8') as icon_file:
                    json.dump(icon_data, icon_file, ensure_ascii=False, indent=2)

            zip_path = os.path.join(output_folder, f'{json_file[:-5]}.zip')
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for icon_file in os.listdir(temp_dir):
                    icon_file_path = os.path.join(temp_dir, icon_file)
                    zipf.write(icon_file_path, icon_file)
                    os.remove(icon_file_path)

            os.rmdir(temp_dir)

    print('Conversion complete.')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert Iconify JSON files to individual zip files."
    )
    parser.add_argument(
        "input_folder",
        nargs='?',
        default='iconify/json',
        help="Path to the folder containing the JSON files"
    )
    parser.add_argument(
        "output_folder",
        nargs='?',
        default='django_svg_icons/data',
        help="Path to the output folder for the zip files"
    )

    args = parser.parse_args()

    extract_iconify_icons(args.input_folder, args.output_folder)
