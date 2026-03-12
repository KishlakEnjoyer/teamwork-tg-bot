# AI Music & Voice Telegram Bot

A Telegram bot built with **aiogram + FastAPI** that provides:

- 🎙 **Voice message recognition** (Speech-to-Text)
- 🎵 **Music search** by:
  - Track title
  - Artist
  - Genre

The bot processes voice input, converts it to text, and allows users to discover music using the **Deezer Public API**.

---

## Project Overview

This project combines Telegram bot interaction, backend API processing, speech recognition, and music search functionality in one system.

Main user scenarios:
- sending a **voice message** and receiving recognized text,
- searching for music by **track name**, **artist**, or **genre**,
- viewing formatted results with track details and Deezer links.

---

## Main Menu Screenshot


![Bot Main Menu](resources/main_menu_screenshot.png)

**Figure 1.** Telegram bot main menu demonstration.


---

## Features

### 1. Voice Recognition
- Accepts Telegram voice messages
- Converts speech to text
- Returns recognized text to the user
- Can be extended for NLP tasks such as emotion detection or intent recognition

### 2. Music Search
Using the **Deezer Public API**, the bot can search music by:
- title,
- artist,
- genre.

The bot returns:
- track name,
- artist,
- album,
- cover image,
- Deezer track link.

### 3. Backend API Integration
The project uses **FastAPI** as a backend service to:
- process requests from the Telegram bot,
- route music search requests,
- handle voice recognition requests,
- validate input and responses,
- centralize business logic.

---

## Used API

### Deezer Public API
The project uses the **Deezer Public API** for music discovery and search.

**Purpose of the API:**
- search tracks by title,
- search music by artist,
- search by genre,
- retrieve track metadata such as:
  - song title,
  - artist name,
  - album title,
  - album cover,
  - direct Deezer link.

This API allows the bot to provide real-time music search results directly inside Telegram.

---

## AI Base Model

**Base AI model used in the project:**  
`d3vastated/whisper-small-ru-en-finetuned`

**Description:**  
This is the base AI model used for multilingual speech recognition in the project. It is a fine-tuned Whisper-based model adapted for **Russian and English speech-to-text recognition**. The model processes Telegram voice messages and converts spoken audio into text that can be returned to the user or used in further NLP tasks.

---

## Transformer Model

**Transformer model used:**  
`d3vastated/whisper-small-ru-en-finetuned`

**Task solved by the transformer model:**  
**Speech-to-Text (automatic speech recognition)**

**Description:**  
The transformer model is used for **voice message transcription**. It receives an audio message from Telegram, processes the speech signal, and generates the recognized text. In this project, the model solves the task of **automatic speech recognition (ASR)** for Russian and English voice input.

---

## Tech Stack

- **Telegram Bot:** aiogram
- **Backend API:** FastAPI
- **Speech Recognition:** `d3vastated/whisper-small-ru-en-finetuned`
- **Music API:** Deezer Public API
- **Language:** Python

---

## Project Structure

```text
project/
│
├── tg-bot/                # Telegram bot (aiogram)
│   ├── handlers/
│   ├── keyboards/
│   └── main.py
│
├── backend/               # FastAPI backend
│   ├── routers/
│   ├── services/
│   └── main.py
│
├── resources/             # Images, screenshots, and static resources
│
├── requirements.txt
├── .env
├── README.md
└── .gitignore
```

---

## Bot Commands

| Command | Description |
| :--- | :--- |
| `/start` | Start the bot |
| `/help` | Show help message |
| `/music` | Search for music |
| `/emotion` | Emotion message classification |
| `Voice message` | Convert speech to text |

---

## Team Members

- **Eric** — Telegram Bot & Deezer Integration
- **Vlad** — AI / Voice Recognition

---

## Task Distribution

### 1. Telegram Bot (aiogram)
**Assigned to:** Eric (Lead)

- Bot command handling (`/start`, `/help`, `/music`)
- Voice message handling
- Message routing
- Middleware
- Integration with FastAPI
- User session handling

**Support:** Vlad (testing & minor features)

### 2. FastAPI Backend
**Shared**

**Eric (Lead)**
- Core FastAPI setup
- API routes for bot integration
- Deezer API service integration
- Request validation
- Error handling

**Vlad (Partial)**
- Voice recognition endpoint
- AI module integration
- Logging

### 3. AI / Speech Recognition Module
**Assigned to:** Vlad (Lead)

- Voice message processing
- Speech-to-text integration
- Text preprocessing
- Future NLP expansion

**Support:** Eric (bot-side formatting & response handling)

### 4. Deezer API Integration
**Assigned to:** Eric (Lead)

- Integration with Deezer Public API
- Searching tracks by:
  - title,
  - artist,
  - genre
- Formatting music results for Telegram
- Handling API limits and response parsing

**Support:** Vlad (optional improvements)

### 5. Testing & QA
**Shared**
- FastAPI endpoint testing
- Bot command testing
- Voice recognition accuracy tests
- End-to-end testing

### 6. Deployment
**Shared**
- Environment setup
- Launch configuration
- Deployment preparation

---

## Summary Table

| Task | Eric | Vlad |
| :--- | :---: | :---: |
| Telegram Bot | Lead | Support |
| FastAPI Core | Lead | Partial |
| Voice Recognition | Support | Lead |
| Deezer API | Lead | Support |
| Testing | Shared | Shared |
| Deployment | Shared | Shared |

---

## Version Control

This project uses **Git** as a version control system.

The remote repository is hosted on **GitHub**, which is used for:
- source code storage,
- collaboration between team members,
- tracking changes,
- maintaining project history.

**Confirmation of version control usage:**
- ✅ Git is used for local version tracking
- ✅ GitHub is used as the remote repository

**GitHub Repository:** `https://github.com/KishlakEnjoyer/teamwork-tg-bot`

---

## Installation and Running

### 1. Clone the repository
```bash
git clone https://github.com/KishlakEnjoyer/teamwork-tg-bot.git
cd teamwork-tg-bot
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

For Windows:
```bash
venv\Scripts\activate
```
ы
### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file and specify the required tokens and settings, for example:
```env
BOT_TOKEN=your_telegram_bot_token
BACKEND_URL=http://localhost:8000
```

### 5. Run the backend
```bash
cd backend
uvicorn main:app --reload
```

### 6. Run the Telegram bot
```bash
cd tg-bot
python main.py
```

---

## Future Improvements

- Improve speech recognition accuracy
- Add better NLP processing
- Extend emotion classification
- Add search filters and recommendations
- Support multilingual voice input
- Improve result formatting and caching

---

## Conclusion

The **AI Music & Voice Telegram Bot** is a practical integration of Telegram bot development, speech recognition, transformer-based AI processing, and music search through the Deezer API.

It demonstrates:
- Telegram bot development with **aiogram**,
- backend service design with **FastAPI**,
- AI module integration for voice processing,
- external API usage with **Deezer**,
- collaboration through **Git** and **GitHub**.
