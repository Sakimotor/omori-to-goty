import os
import yaml
import json
import argparse

# Chemin de base de l'arborescence de dossiers
def folder_to_json(base_path, output='steam_languageData.json'):

    result = {}

    # Pour chaque dossier de langue
    for lang_folder in os.listdir(base_path):
        lang_path = os.path.join(base_path, lang_folder)
        if os.path.isdir(lang_path):
            result[lang_folder] = {}
            result[lang_folder]['text'] = {}
            # Pour chaque fichier .yaml dans le dossier de langue
            for yaml_file in os.listdir(lang_path):
                if yaml_file.endswith('.yaml'):
                    file_path = os.path.join(lang_path, yaml_file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        # Charger le contenu du fichier .yaml en utilisant la librairie yaml
                        yaml_content = yaml.load(f, Loader=yaml.FullLoader)
                        # Ajouter le contenu au dictionnaire
                        result[lang_folder]['text'][yaml_file.split('.')[0]] = yaml_content

                    with open(output, 'wb') as f:
                        f.write(json.dumps(result, ensure_ascii=False, indent=4).encode('utf-8'))

def json_merge(st, sw, output = 'merged.json'):
    with open(sw, 'rb') as file1, open(st, 'rb') as file2:
        json_switch = json.load(file1)
        json_steam = json.load(file2)
        update_json(json_switch, json_steam)

    with open(output, 'wb') as f:
        f.write(json.dumps(json_switch, ensure_ascii=False, indent=4).encode('utf-8'))


def update_json(json1, json2):
    for key in json2:
        if key in json1 and json1[key] is not None:
            if isinstance(json1[key], dict) and isinstance(json2[key], dict):
                update_json(json1[key], json2[key])
            else:
                json1[key] = json2[key]


def main():
    parser = argparse.ArgumentParser(description='Permet de créer un fichier .json à partir du dossier languages Steam.')
    parser.add_argument('-m', '--merge', nargs=2, metavar=('steam', 'switch'), help='Remplace les valeurs du fichier JSON Switch avec celui généré')
    parser.add_argument('-i', '--input', metavar='path', default='.', help='Chemin vers le dossier languages')
    parser.add_argument("-o", "--output", help="Le nom de sortie du fichier JSON")
    args = parser.parse_args()

    if args.merge:
        if args.output:
            json_merge(*args.merge, output = args.output)
        else:
            json_merge(*args.merge)
    elif args.input:
        if args.output:
            folder_to_json(args.input, output = args.output)
        else:
            folder_to_json(args.input)
    else:
        if args.output:
            folder_to_json('.', output = args.output)
        else:
            folder_to_json('.')


if __name__ == '__main__':
    main()
