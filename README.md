# 🌍 AI Translator

> **Translate Anything. Anywhere. Simply.**

A professional multilingual translation application built with Python and LibreTranslate.

## ✨ Features

- 🌍 Multilingual translation
- 🔎 Automatic source-language detection
- 🎯 Target language selection
- 🇮🇷 Persian language support
- 📚 Translation history
- 🗑️ Clear translation history
- 🧩 Modular project architecture
- 🛡️ Error handling
- 🔌 Local LibreTranslate server
- 💻 Runs locally on your computer
- 🚫 No paid AI API required

## 🛠️ Technologies

- Python 3
- LibreTranslate
- Requests
- Git
- GitHub

## 📁 Project Structure

```text
AI-Translator/
│
├── main.py
├── translator.py
├── history.py
├── exceptions.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
└── translation_history.json
🚀 Installation
1. Clone the repository
git clone https://github.com/QeYsAr-Dev/AI-Translator.git
cd AI-Translator
2. Create a virtual environment
Windows PowerShell:
python -m venv venv
3. Activate the virtual environment
.\venv\Scripts\Activate.ps1
4. Install dependencies
pip install -r requirements.txt
▶️ Start LibreTranslate
Run:
libretranslate --host 127.0.0.1 --port 5000
Keep this terminal running.
▶️ Run AI Translator
Open a second terminal and activate the virtual environment:
.\venv\Scripts\Activate.ps1
Then run:
python main.py
🌐 Languages
AI Translator automatically loads the languages available from the LibreTranslate server.
The application is designed to support multiple languages rather than being limited to Persian and English.
📚 Translation History
Translations are automatically saved locally so previous translations can be viewed later.
You can also clear the entire translation history from the application menu.
🔐 Security
Sensitive files such as .env are excluded using .gitignore.
Never publish API keys, passwords, tokens, or other private credentials on GitHub.
🧩 Architecture
The project uses a modular structure:
main.py — Application interface and menu
translator.py — Translation and language detection
history.py — Translation history management
exceptions.py — Custom application errors
config.py — Configuration
requirements.txt — Python dependencies
🎯 Project Goal
The goal of AI Translator is to provide a simple, professional, and extensible multilingual translation tool that can run locally without depending on a paid AI API.
🔮 Future Improvements
Planned improvements may include:
Graphical User Interface (GUI)
Voice input
Text-to-speech
File translation
Batch translation
More translation providers
Provider switching
Translation quality improvements
Dark mode
Modern desktop interface
👨‍💻 Author
QeYsAr-Dev
GitHub:
https://github.com/QeYsAr-Dev
⭐ Support
If you find this project useful, consider giving it a ⭐ on GitHub.