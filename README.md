# MS Teams Transcript Exporter

A Python-based automation tool built with Selenium to streamline the process of capturing meeting and lecture transcripts from Microsoft Teams. This tool is designed to help students and professionals easily grab transcripts for offline studying and note-taking.

## 🚀 Features
* **Automated Extraction:** Scrapes and consolidates transcript blocks using Selenium WebDriver.
* **Clipboard Integration:** Instantly copies the full consolidated transcript to your clipboard, ready to be pasted straight into your favorite note-taking app (Notion, Obsidian, Word, etc.).

## 🛠️ Prerequisites
Before running the script, ensure you have the following installed:
* Python 3.8 or higher
* Google Chrome (or Microsoft Edge)
* A matching version of WebDriver (automatically handled if using `webdriver-manager` or configured locally)

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd teams-transcript-exporter
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage
Run the main script to start the automation process:
```bash
python main.py
```
Once execution finishes, the complete transcript text will be waiting in your **clipboard**. Just press `Ctrl+V` (or `Cmd+V` on Mac) to paste it anywhere.

## 📅 Roadmap (Upcoming Features)
* [ ] **Direct File Export:** Automatically save the transcripts as timestamped `.txt` and `.md` files without relying on the clipboard.

## 🔒 Privacy & Security First
This project strictly enforces credential isolation. 
* **Never** hardcode your email or password in `main.py`.
* Ensure that `.env`, `__pycache__/`, and any generated files are added to your `.gitignore` file before pushing any code to GitHub.

## ⚖️ Disclaimer
This project was developed strictly for personal educational purposes, study assistance, and accessibility research. It is **not** affiliated with, authorized, or endorsed by Microsoft Corporation. 

Users are entirely responsible for ensuring compliance with Microsoft Teams' Terms of Service, as well as the internal privacy policies and intellectual property guidelines of their respective academic institutions or workplaces. The developer assumes no liability for any misuse or policy violations resulting from this tool.
