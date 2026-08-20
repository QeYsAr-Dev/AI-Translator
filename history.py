import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class TranslationHistory:
    def __init__(self, file_path: str) -> None:
        self.file_path = Path(file_path)

    def _load(self) -> list[dict[str, Any]]:
        if not self.file_path.exists():
            return []

        try:
            with self.file_path.open(
                "r",
                encoding="utf-8",
            ) as file:
                data = json.load(file)

            if isinstance(data, list):
                return data

            return []

        except (json.JSONDecodeError, OSError):
            return []

    def _save(self, data: list[dict[str, Any]]) -> None:
        with self.file_path.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4,
            )

    def add(
        self,
        source_text: str,
        target_language: str,
        translation: str,
    ) -> None:
        history = self._load()

        history.append(
            {
                "source_text": source_text,
                "target_language": target_language,
                "translation": translation,
                "timestamp": datetime.now(
                    timezone.utc
                ).isoformat(),
            }
        )

        self._save(history)

    def get_all(self) -> list[dict[str, Any]]:
        return self._load()

    def clear(self) -> None:
        self._save([])