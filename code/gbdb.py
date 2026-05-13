from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent
PATH_MASTER_FILE = BASE_DIR / "database" / "master.json"

class MasterClass:
    def __init__(self) -> None:
        self.load_master_file()

    def load_master_file(self):
        with open(PATH_MASTER_FILE, "r", encoding="utf-8") as f:
            self.master = json.load(f)


Master = MasterClass()

elements = Master.master["elements"]
weapons = Master.master["weapons"]



