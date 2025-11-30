# 🤖 Jarvis AI – Your Personal Desktop Assistant
An intelligent AI-powered voice assistant built with Python and OpenAI’s GPT models. Jarvis can chat, open websites and apps, play music, tell the time, and save AI-generated responses to files. Designed to be modular, scalable, and extendable.


[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)


---

## 🚀 Overview

**Jarvis AI** is a **desktop-based intelligent AI assistant** built with **Python** and **OpenAI GPT-4o-mini**. Inspired by Iron Man’s Jarvis, it enables you to:

- Chat naturally with AI  
- Respond to **voice commands**  
- Open websites and desktop apps  
- Play local music files  
- Announce the **current time**  
- Save AI responses to files  
- Gracefully handle OpenAI quota limits  

Jarvis runs on macOS using the `say` command for voice output and is **extensible to Windows/Linux** with minor adjustments.

---

## 🌟 Key Features

| Feature | Description |
|---------|-------------|
| 💬 AI Chat | Chat with GPT-4o-mini for conversation or guidance |
| 🎤 Voice Commands | Speak to Jarvis for hands-free control |
| 🌐 Web Launcher | Open YouTube, Google, Wikipedia, or custom sites |
| 🎵 Music Player | Play local audio files instantly |
| 🕒 Time Teller | Get the current time in voice format |
| 🗂 Save Responses | Store AI responses to text files |
| 🔄 Reset Chat | Clear conversation history anytime |
| ⚠️ Quota Handling | Friendly message when API quota is exceeded |

---

## 🛠 Technology Stack

- **Python 3.10+**  
- **OpenAI GPT-4o-mini** for AI responses  
- **SpeechRecognition** for microphone input  
- **MacOS say command** for voice output  
- **Random & Datetime** for file management & time features  

---

## 🎨 Demo

### Chat & Voice Interaction:

![Jarvis Chat Demo](assets/demo.gif)  

> Jarvis listens, responds, and executes commands seamlessly.

---
## 💻 Installation Guide

### All-in-One Setup
```bash
# 1️⃣ Clone the Repository
git clone https://github.com/<your-username>/JarvisAI.git
cd JarvisAI

# 2️⃣ Create Virtual Environment
python3 -m venv .venv

# Activate the environment
# Mac/Linux
source .venv/bin/activate
# Windows
.venv\Scripts\activate

# 3️⃣ Install Dependencies
pip install -r requirements.txt

# 4️⃣ Add OpenAI API Key
# Create a file named config.py and add your API key:
# apikey = "YOUR_OPENAI_API_KEY"

# 5️⃣ Run Jarvis AI
python main.py


🖥 Usage Instructions
Speak or type commands into Jarvis:
Command	Action
open youtube	Opens YouTube in browser
open google	Opens Google in browser
open wikipedia	Opens Wikipedia in browser
open music	Plays your local music file
the time	Announces current time
open facetime	Opens FaceTime app
open pass	Opens Passky app
using artificial intelligence	Saves AI response to a file
reset chat	Clears conversation history
jarvis quit	Exits Jarvis AI
⚠️ Update paths for music and apps based on your system.


---
## 💻 Installation Guide

## 📂 Project Structure

Below is the complete structure of the **JarvisAI** project:

```text
JarvisAI/
│
├── main.py                  # Core voice assistant script
├── config.py                # API key configuration
├── requirements.txt         # Python dependencies
├── Openai/                  # Folder for AI-generated text files
├── assets/                  # Screenshots, GIFs, icons
└── README.md                # Project documentation

---
## 💻 Installation Guide

## 👤 Author

**SARANG ANUPAM**  

*"Jarvis AI – Your personal assistant for productivity, learning, and fun!"*

