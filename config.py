import os

from dotenv import load_dotenv


load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MODEL = os.getenv("OPENAI_MODEL", "gpt-5.6-luna")

HISTORY_FILE = os.getenv(
    "HISTORY_FILE",
    "translation_history.json",
)


if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY is not configured. "
        "Please create a .env file and add your API key."
    )