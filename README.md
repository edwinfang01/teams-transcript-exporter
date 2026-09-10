# MS Teams Transcript Exporter

A Python-based automation tool built with Selenium to streamline the process of capturing meeting and lecture transcripts from Microsoft Teams. This tool is designed to help students and professionals easily grab transcripts for offline studying and note-taking.

## 🚀 Features
* **Automated Extraction:** Scrapes and consolidates transcript blocks using Selenium WebDriver.
* **Direct File Export:** Automatically saves the transcripts as clean `.txt` files to a specified local directory using `pathlib`.
* **Cross-Platform Path Handling:** Uses robust path definitions compatible with Windows, macOS, and Linux.

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

## ⚙️ Configuration
Open your script file and configure your target file name and local directory path:

```python
FILE_NAME = "your transcript file name"
SAVE_PATH = Path(rf"the path where you want to save your file eg. C:\Users\username\Downloads") / f"{FILE_NAME}.txt"
```

## 💻 Usage
Run the main script to start the automation process:
```bash
python main.py
```
Once the execution finishes, you will find your transcript text file saved automatically at your configured `SAVE_PATH`.

## 📅 Roadmap (Upcoming Features)
* [ ] **Clipboard Integration:** Option to instantly copy the full consolidated transcript to your clipboard.
* [ ] **Environment Variables (`.env`):** Move credentials and personal system paths out of the source code to keep local environments 100% private.

## ⚖️ Disclaimer
This project was developed strictly for personal educational purposes, study assistance, and accessibility research. It is **not** affiliated with, authorized, or endorsed by Microsoft Corporation. 

Users are entirely responsible for ensuring compliance with Microsoft Teams' Terms of Service, as well as the internal privacy policies and intellectual property guidelines of their respective academic institutions or workplaces. The developer assumes no liability for any misuse or policy violations resulting from this tool.

