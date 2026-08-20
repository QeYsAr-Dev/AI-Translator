from translator import Translator
from exceptions import TranslationError


def print_header() -> None:
    print("\n" + "=" * 70)
    print("                         AI TRANSLATOR")
    print("=" * 70)
    print("        Multi-language translation powered by LibreTranslate")
    print("=" * 70)


def get_non_empty_input(prompt: str) -> str:
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_languages(translator: Translator) -> list[dict]:
    try:
        return translator.get_languages()
    except TranslationError as error:
        print(f"\nError loading languages: {error}")
        return []


def display_languages(languages: list[dict]) -> None:
    print("\nAvailable Languages")
    print("-" * 70)

    for index, language in enumerate(languages, start=1):
        name = language.get("name", "Unknown")
        code = language.get("code", "??")

        print(f"{index:>3}. {name:<30} [{code}]")

    print("-" * 70)


def choose_target_language(
    languages: list[dict],
) -> str | None:

    if not languages:
        return None

    display_languages(languages)

    while True:
        choice = input(
            "\nEnter language code "
            "(example: fa, en, de): "
        ).strip().lower()

        if any(
            language.get("code") == choice
            for language in languages
        ):
            return choice

        print(
            "Invalid language code. "
            "Please choose a code from the list."
        )


def translate_mode(translator: Translator) -> None:
    print("\n" + "-" * 70)
    print("TRANSLATION MODE")
    print("-" * 70)

    text = get_non_empty_input(
        "\nEnter text to translate:\n> "
    )

    print("\nDetecting source language...")

    try:
        source_language = translator.detect_language(text)

        print(
            f"Detected source language: "
            f"{source_language}"
        )

    except TranslationError as error:
        print(f"\nLanguage detection failed: {error}")
        return

    languages = get_languages(translator)

    if not languages:
        return

    target_language = choose_target_language(
        languages
    )

    if target_language is None:
        return

    if target_language == source_language:
        print(
            "\nTarget language is the same as "
            "the detected source language."
        )

        retry = input(
            "Do you want to continue anyway? (y/n): "
        ).strip().lower()

        if retry != "y":
            return

    print("\nTranslating...")

    try:
        result = translator.translate(
            text=text,
            target_language=target_language,
            source_language=source_language,
        )

        print("\n" + "=" * 70)
        print("TRANSLATION RESULT")
        print("=" * 70)
        print(result)
        print("=" * 70)

    except TranslationError as error:
        print(f"\nTranslation error: {error}")


def show_languages_mode(
    translator: Translator,
) -> None:

    print("\n" + "-" * 70)
    print("AVAILABLE LANGUAGES")
    print("-" * 70)

    languages = get_languages(translator)

    if languages:
        display_languages(languages)


def history_mode(translator: Translator) -> None:
    history = translator.get_history()

    print("\n" + "-" * 70)
    print("TRANSLATION HISTORY")
    print("-" * 70)

    if not history:
        print("No translation history found.")
        return

    for index, item in enumerate(
        history,
        start=1,
    ):
        print(f"\n[{index}]")
        print(f"Source: {item['source_text']}")
        print(
            f"Target language: "
            f"{item['target_language']}"
        )
        print(
            f"Translation: "
            f"{item['translation']}"
        )
        print(
            f"Time: "
            f"{item['timestamp']}"
        )

    print("\n" + "-" * 70)


def clear_history_mode(
    translator: Translator,
) -> None:

    history = translator.get_history()

    if not history:
        print("\nTranslation history is already empty.")
        return

    confirmation = input(
        "\nAre you sure you want to clear "
        "all translation history? (y/n): "
    ).strip().lower()

    if confirmation == "y":
        translator.clear_history()
        print("\nTranslation history cleared.")
    else:
        print("\nOperation cancelled.")


def show_menu() -> None:
    print("\n")
    print("1. Translate text")
    print("2. View translation history")
    print("3. Clear translation history")
    print("4. Show available languages")
    print("5. Exit")


def main() -> None:
    print_header()

    print("\nConnecting to LibreTranslate...")

    try:
        translator = Translator()

    except TranslationError as error:
        print(f"\nStartup error: {error}")
        print(
            "\nMake sure LibreTranslate is running on:"
        )
        print("http://127.0.0.1:5000")
        return

    print("Connected successfully.")

    while True:
        show_menu()

        choice = input(
            "\nEnter your choice: "
        ).strip()

        if choice == "1":
            translate_mode(translator)

        elif choice == "2":
            history_mode(translator)

        elif choice == "3":
            clear_history_mode(translator)

        elif choice == "4":
            show_languages_mode(translator)

        elif choice == "5":
            print(
                "\nThank you for using AI Translator."
            )
            print("Goodbye!")
            break

        else:
            print(
                "\nInvalid choice. "
                "Please select 1, 2, 3, 4, or 5."
            )


if __name__ == "__main__":
    main()