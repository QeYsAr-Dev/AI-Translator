<div align="center">

# 🌍 AI Translator

### 💡 From Concept To Creation

**🐍 Python • 🤖 AI Translation • 🌐 LibreTranslate • 📚 NLP**

<p>
  <a href="https://github.com/QeYsAr-Dev/AI-Translator">
    <img src="https://img.shields.io/badge/GitHub-AI--Translator-black?style=for-the-badge&logo=github" alt="GitHub">
  </a>
  <img src="https://img.shields.io/badge/Python-3-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/LibreTranslate-API-orange?style=for-the-badge" alt="LibreTranslate">
  <img src="https://img.shields.io/badge/NLP-Multilingual-purple?style=for-the-badge" alt="NLP">
</p>

<p>
  A professional multilingual translation application built with Python and LibreTranslate.
</p>

</div>

---

## 📖 About

**AI Translator** is a Python-based multilingual translation application designed to provide a simple, practical, and extensible translation experience.

The application communicates with a local **LibreTranslate** server to translate text, detect source languages, and work with multiple target languages.

It also includes a local translation history system, modular architecture, custom error handling, and configuration management.

> **Translate Anything. Anywhere. Simply.**

---

## ✨ Features

* 🌍 **Multilingual Translation**
* 🔎 **Automatic Source-Language Detection**
* 🎯 **Target Language Selection**
* 🇮🇷 **Persian Language Support**
* 📚 **Translation History**
* 🗑️ **Clear Translation History**
* 🔌 **Local LibreTranslate Integration**
* 💻 **Runs Locally**
* 🚫 **No Paid AI API Required**
* 🧩 **Modular Architecture**
* 🛡️ **Custom Error Handling**
* ⚙️ **Configuration Management**

---

## 🛠️ Technologies

<div align="center">

### 🐍 Programming Language

<img src="https://skillicons.dev/icons?i=python" alt="Python">

### 🌐 Translation Engine

`LibreTranslate` • `REST API`

### 📡 HTTP Communication

`Requests`

### 🔧 Development

<img src="https://skillicons.dev/icons?i=git,github,vscode" alt="Development Tools">

</div>

---

## 📂 Project Structure

```text
AI-Translator/
│
├── 🚀 main.py
├── 🌐 translator.py
├── 📚 history.py
├── ⚠️ exceptions.py
├── ⚙️ config.py
├── 📦 requirements.txt
├── 💾 translation_history.json
├── ⚙️ .gitignore
└── 📖 README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/QeYsAr-Dev/AI-Translator.git
cd AI-Translator
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate the Virtual Environment

#### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🌐 Start LibreTranslate

Start the local LibreTranslate server:

```bash
libretranslate --host 127.0.0.1 --port 5000
```

Keep the LibreTranslate terminal running.

Then open another terminal, activate the virtual environment, and run:

```bash
python main.py
```

---

## 🔄 How It Works

<div align="center">

### 📝 Enter Text

↓

### 🔎 Detect Source Language

↓

### 🌐 Select Target Language

↓

### 🔌 Send Request to LibreTranslate

↓

### 🤖 Process Translation

↓

### 📚 Save Translation History

↓

### ✅ Display Result

</div>

---

## 🧩 Architecture

The project follows a modular structure where each component has a specific responsibility:

|        File        | Responsibility                     |
| :----------------: | ---------------------------------- |
|      `main.py`     | Application interface and menu     |
|   `translator.py`  | Translation and language detection |
|    `history.py`    | Translation history management     |
|   `exceptions.py`  | Custom application errors          |
|     `config.py`    | Application configuration          |
| `requirements.txt` | Python dependencies                |

This structure keeps the project organized and makes future improvements easier.

---

## 📚 Translation History

Translations are stored locally so previous translations can be viewed later.

The application also provides an option to clear the saved translation history.

This makes the project more useful as a practical everyday translation tool while keeping the data locally managed.

---

## 🔐 Security

The project is designed to run locally and avoids requiring a paid AI API.

Sensitive configuration files should never contain credentials that are committed to GitHub.

> **Never publish API keys, passwords, tokens, or other private credentials.**

---

## 🧠 What I Learned

Building this project helped strengthen several important development concepts:

* 🐍 Python application architecture
* 🌐 REST API integration
* 📡 HTTP requests
* 🤖 Machine translation concepts
* 🔎 Language detection
* 🧩 Modular programming
* 📚 Local data persistence
* ⚠️ Custom exception handling
* ⚙️ Configuration management
* 🧠 Problem-solving and debugging

---

## 🔮 Future Improvements

Possible future improvements include:

* [ ] 🖥️ Add a modern GUI
* [ ] 🎤 Add voice input
* [ ] 🔊 Add text-to-speech
* [ ] 📄 Add file translation
* [ ] 📦 Add batch translation
* [ ] 🌐 Support additional translation providers
* [ ] 🔄 Add translation-provider switching
* [ ] 🎯 Improve translation quality
* [ ] 🌙 Add dark mode
* [ ] 🖥️ Build a modern desktop interface

---

## 📈 Project Status

<div align="center">

### 🟢 Active Development

The current version provides a functional local multilingual translation system with LibreTranslate integration, translation history, and a modular Python architecture.

</div>

---

## 👨‍💻 Author

<div align="center">

### QeYsAr

**🐍 Python Developer | 🤖 AI Enthusiast | 💻 Developer**

<a href="https://github.com/QeYsAr-Dev">
  <img src="https://img.shields.io/badge/GitHub-QeYsAr--Dev-black?style=for-the-badge&logo=github" alt="GitHub Profile">
</a>

</div>

---

<div align="center">

### ⭐ If you like this project, consider giving it a star!

**Keep Learning. Keep Building. Keep Creating. 🚀**

</div>
