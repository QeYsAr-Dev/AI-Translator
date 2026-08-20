import requests

from config import HISTORY_FILE
from exceptions import TranslationError
from history import TranslationHistory


class Translator:
    """Translation service powered by a local LibreTranslate server."""

    def __init__(
        self,
        base_url: str = "http://127.0.0.1:5000",
        timeout: int = 60,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.history = TranslationHistory(HISTORY_FILE)

        self._check_connection()

    def _check_connection(self) -> None:
        """Check that the LibreTranslate server is available."""

        try:
            response = requests.get(
                f"{self.base_url}/languages",
                timeout=5,
            )
            response.raise_for_status()

        except requests.RequestException as error:
            raise TranslationError(
                "Could not connect to LibreTranslate. "
                "Make sure the LibreTranslate server is running "
                "on http://127.0.0.1:5000."
            ) from error

    def get_languages(self) -> list[dict]:
        """Get all languages currently available."""

        try:
            response = requests.get(
                f"{self.base_url}/languages",
                timeout=self.timeout,
            )
            response.raise_for_status()

            data = response.json()

            if not isinstance(data, list):
                raise TranslationError(
                    "LibreTranslate returned an invalid language list."
                )

            return data

        except requests.RequestException as error:
            raise TranslationError(
                f"Could not retrieve languages: {error}"
            ) from error

        except ValueError as error:
            raise TranslationError(
                "LibreTranslate returned invalid JSON."
            ) from error

    def get_language_codes(self) -> list[str]:
        """Return the language codes supported by the server."""

        languages = self.get_languages()

        return [
            language["code"]
            for language in languages
            if isinstance(language, dict)
            and language.get("code")
        ]

    def detect_language(self, text: str) -> str:
        """Automatically detect the language of the provided text."""

        text = text.strip()

        if not text:
            raise TranslationError(
                "Text cannot be empty."
            )

        try:
            response = requests.post(
                f"{self.base_url}/detect",
                data={"q": text},
                timeout=self.timeout,
            )
            response.raise_for_status()

            data = response.json()

            if not isinstance(data, list) or not data:
                raise TranslationError(
                    "LibreTranslate could not detect the language."
                )

            language = data[0].get("language")

            if not language:
                raise TranslationError(
                    "No language code was returned."
                )

            return language

        except requests.RequestException as error:
            raise TranslationError(
                f"Language detection failed: {error}"
            ) from error

        except (ValueError, AttributeError, IndexError) as error:
            raise TranslationError(
                "Invalid response from language detection."
            ) from error

    def translate(
        self,
        text: str,
        target_language: str,
        source_language: str = "auto",
    ) -> str:
        """Translate text from a source language to a target language."""

        text = text.strip()
        target_language = target_language.strip().lower()
        source_language = source_language.strip().lower()

        if not text:
            raise TranslationError(
                "Source text cannot be empty."
            )

        if not target_language:
            raise TranslationError(
                "Target languagecannot be empty."
            )

        available_languages = self.get_language_codes()

        if target_language not in available_languages:
            raise TranslationError(
                f"Target language '{target_language}' "
                "is not available on this server."
            )

        if source_language == "auto":
            source_language = self.detect_language(text)

        if source_language not in available_languages:
            raise TranslationError(
                f"Source language '{source_language}' "
                "is not available on this server."
            )

        try:
            response = requests.post(
                f"{self.base_url}/translate",
                data={
                    "q": text,
                    "source": source_language,
                    "target": target_language,
                    "format": "text",
                },
                timeout=self.timeout,
            )

            response.raise_for_status()

            data = response.json()

            if not isinstance(data, dict):
                raise TranslationError(
                    "LibreTranslate returned an invalid response."
                )

            translation = data.get("translatedText")

            if not translation:
                raise TranslationError(
                    "LibreTranslate returned an empty translation."
                )

            self.history.add(
                source_text=text,
                target_language=target_language,
                translation=translation,
            )

            return translation.strip()

        except TranslationError:
            raise

        except requests.RequestException as error:
            raise TranslationError(
                f"Translation request failed: {error}"
            ) from error

        except (ValueError, AttributeError) as error:
            raise TranslationError(
                "Invalid translation response received."
            ) from error

    def get_history(self) -> list[dict]:
        """Return all saved translations."""

        return self.history.get_all()

    def clear_history(self) -> None:
        """Clear all saved translation history."""

        self.history.clear()