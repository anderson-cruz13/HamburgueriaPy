import json
import os
from typing import Dict, Any


class SaveJson:
    def __init__(self, name_file: str) -> None:
        self.path = os.path.join("./data/arquivos_json")
        os.makedirs(self.path, exist_ok=True)
        self.file = os.path.join(self.path, name_file)

    def _create_json(self, data: Dict[str, Any]) -> None:
        if not os.path.exists(self.file):
            with open(self.file, 'w', encoding="utf8") as arq:
                json.dump(data, arq, indent=4, ensure_ascii=False)

    def modify_json(self, data: Dict[str, Any]) -> None:
        if os.path.exists(self.file):
            existing_data = self.load_json()
            existing_data.update(data)
            with open(self.file, 'w', encoding="utf8") as arq:
                json.dump(existing_data, arq, indent=4, ensure_ascii=False)
        else:
            self._create_json(data)

    def update_json(self, data: Dict[str, Any]) -> None:
        with open(self.file, "w", encoding="utf8") as arq:
            json.dump(data, arq, indent=4, ensure_ascii=False)

    def load_json(self) -> Dict[str, Any]:
        if os.path.exists(self.file):
            with open(self.file, 'r', encoding="utf8") as arq:
                return json.load(arq)
        else:
            self._create_json({})
            return {}
