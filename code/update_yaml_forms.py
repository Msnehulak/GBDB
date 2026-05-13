from pathlib import Path
import json
import gbdb
import os

BASE_DIR = Path(__file__).resolve().parent.parent
GIT_YAML_PATH = BASE_DIR / ".github" / "ISSUE_TEMPLATE"

print(os.listdir(GIT_YAML_PATH))

class YamlCreateClass:
    
    @staticmethod
    def head(name = "name",
             description = "description",
            ):
        return f"""name: {name}
description: {description}
body:
"""
    
    @staticmethod
    def markdown(value = "pepa" ):
        return f"""  - type: markdown
    attributes:
      value: |
        {value}
"""
    
    @staticmethod
    def input(id = "id", label="label", description="description", required: bool = True):
        return f"""  - type: input
    id: {id}
    attributes:
      label: {label}
      description: {description}
      placeholder: ex. email@example.com
    validations:
      required: {required}
"""

class YamlClass:
    def __init__(self) -> None:
        self.add = YamlCreateClass()

    def create_yaml(self):
        add = self.add
        yaml = ""
        yaml += add.head()
        yaml += add.markdown()
        print(yaml)

app = YamlClass()
app.create_yaml()
