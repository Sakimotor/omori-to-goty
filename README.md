# omori-to-goty
**WIP** Script that converts the translation files from Omori's Steam languages folder into the Switch (all GOTY versions behave the same ?) languagesData.json file.

##Usage:
```
usage: langfolder_to_json.py [-h] [-m steam switch] [-i path] [-o OUTPUT]

Permet de créer un fichier .json à partir du dossier languages Steam.

optional arguments:
  -h, --help            show this help message and exit
  -m steam switch, --merge steam switch
                        Remplace les valeurs du fichier JSON Switch avec celui généré
  -i path, --input path
                        Chemin vers le dossier languages
  -o OUTPUT, --output OUTPUT
                        Le nom de sortie du fichier JSON
```
