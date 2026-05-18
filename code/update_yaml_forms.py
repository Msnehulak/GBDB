
from pathlib import Path
import json
import gbdb
import os
import yaml

BASE_DIR = Path(__file__).resolve().parent.parent
PATH_YAMAL_FORMS = BASE_DIR / ".github" / "ISSUE_TEMPLATE"

class YamlClass:
    def __init__(self, name="Custom Issue", description="Popis šablony", labels = ["new-character"]):
        self.data = {
            "name": name,
            "description": description,
            "labels": labels,
            "body": [],
        }

    def add_markdown(self, value="Text v markdownu"):
        self.data["body"].append({
            "type": "markdown",
            "attributes": {
                "value": value
            }
        })

    def add_input(self, id, label, description="", placeholder="ex. email@example.com", required=True):
        self.data["body"].append({
            "type": "input",
            "id": id,
            "attributes": {
                "label": label,
                "description": description,
                "placeholder": placeholder
            },
            "validations": {
                "required": required
            }
        })

    def add_dropdown(self, id, label, options, required=True):
        self.data["body"].append({
            "type": "dropdown",
            "id": id,
            "attributes": {
                "label": label,
                "options": options
            },
            "validations": {
                "required": required
            }
        })

    def generate_yaml(self):
        # sort_keys=False zachová pořadí, v jakém jsi data přidával
        # allow_unicode=True zajistí správné zobrazení češtiny
        return yaml.dump(self.data, sort_keys=False, allow_unicode=True, default_flow_style=False)

    def save_to_file(self, filename):
        path = Path(filename)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(self.generate_yaml())
        print(f"Šablona byla uložena do: {path.absolute()}")

class Generate:
    @staticmethod
    def character():
        gen = YamlClass(name="Add character", description="add new Genshin Impact character to database", labels=["new-character"])
        gen.add_input(id="name", label="Character name", description="Name of Character", placeholder="Character Name")
        gen.add_dropdown(id = "element", label="Element", options=gbdb.elements)
        gen.add_dropdown(id = "weapon", label="Weapon", options=gbdb.weapons)
        gen.add_dropdown(id = "region", label="Region", options=gbdb.regions)


        gen.save_to_file(PATH_YAMAL_FORMS / "add_character.yaml")
        print(gen.generate_yaml())

gen = Generate()
gen.character()

