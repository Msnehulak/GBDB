from pathlib import Path
import os
import re
import json

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_DIR = BASE_DIR / "database"

class IssueWorker:
    def __init__(self) -> None:
        self.issue_body = os.environ.get("ISSUE_BODY", "").replace("\r\n", "\n")
        self.clear_data()    
        self.find_issue_type()
        self.run()

    def clear_data(self):
        data = {}
        sections = re.split(r'###\s+', self.issue_body)
       
        for section in sections:
            if not section.strip():
                continue
            lines = section.split('\n', 1)
            key = lines[0].strip().lower().replace(" ", "_")
            value = lines[1].strip() if len(lines) > 1 else ""

            data[key] = value.strip()
            
        self.issue_data = data

    def find_issue_type(self):
        if 'character_name' in self.issue_data:
            self.issue_type = 'new-character'
        else:
            self.issue_type = 'idk'

    @staticmethod
    def save_data(path, data, save_message):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
                
        print(f"{save_message} {path}")

    def run(self):
        print(f"Form type is: {self.issue_type}")
        
        if self.issue_type == 'new-character':
            char_id = self.issue_data.get("character_name", "unknown").lower().replace(" ", "-")
            
            character_json = {
                "id": char_id,
                "name": self.issue_data.get("character_name", "unknown name"),
                "element": self.issue_data.get("element", ""),
                "weapon_type": self.issue_data.get("weapon", ""),
                "region": self.issue_data.get("region", ""),
                "description": ""
            }
            output_dir = DATABASE_DIR / "characters"
            output_dir.mkdir(parents=True, exist_ok=True)
            output_file = output_dir / f"{char_id}.json"
            
            self.save_data(output_file, character_json, 'character is successfully seved as:')

        elif self.issue_type == 'idk':
            print("unknown form type, passing to next.")

if __name__ == "__main__":
    app = IssueWorker()
    print(app.issue_type, app.issue_data)
