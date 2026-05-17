import os
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_DIR = BASE_DIR / "database"

def parse_markdown_issue(issue_body):
    """
    Jednoduchý parser, který vytáhne data z textu GitHub Issue.
    Hledá nadpisy formuláře (uvedené jako ### Název) a text pod nimi.
    """
    data = {}
    # Rozdělíme text podle nadpisů markdownu, které generuje GitHub Issue formát
    sections = re.split(r'###\s+', issue_body)
    
    for section in sections:
        if not section.strip():
            continue
        lines = section.split('\n', 1)
        key = lines[0].strip().lower().replace(" ", "_")
        value = lines[1].strip() if len(lines) > 1 else ""
        
        # Očištění od případných prázdných řádků na konci
        data[key] = value.strip()
        
    return data

def main():
    # GitHub Actions ukládá text celého Issue do environmentální proměnné
    issue_body = os.environ.get("ISSUE_BODY", "")
    
    if not issue_body:
        print("Žádná data z Issue nebyla nalezena.")
        return

    # Parsování dat z formuláře
    parsed_data = parse_markdown_issue(issue_body)
    
    # Získání ID postavy pro název souboru (např. raiden-shogun)
    # Pokud v novém formuláři nemáš přímo pole ID, můžeš použít očištěné jméno
    char_id = parsed_data.get("id_postavy", parsed_data.get("character_name", "unknown")).lower().replace(" ", "-")
    
    # Sestavení finální struktury podle tvého doc/characters.md
    character_json = {
        "id": char_id,
        "name": parsed_data.get("character_name", "Neznámé jméno"),
        "element": parsed_data.get("element", ""),
        "description": parsed_data.get("popis_talentů", "")
        # Sem si pak doplníš další pole podle potřeby
    }
    
    # Uložení do souboru database/characters/{char_id}.json
    # Doporučuji ukládat postavy samostatně, ať se ti master.json nezačne hned kousat
    output_dir = DATABASE_DIR / "characters"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_file = output_dir / f"{char_id}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(character_json, f, indent=4, ensure_ascii=False)
        
    print(f"Postava úspěšně uložena do {output_file}")

if __name__ == "__main__":
    main()
