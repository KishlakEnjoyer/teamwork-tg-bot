⸻

🎵🎙 AI Music & Voice Telegram Bot

A Telegram bot built with aiogram + FastAPI that provides:
 • 🎙 Voice message recognition (Speech-to-Text)
 • 🎵 Music search by:
   • Track name
   • Artist
   • Genre

The bot processes voice input, converts it to text, and allows users to discover music using the Deezer API.

⸻

🚀 Features

🎙 1. Voice Recognition
 • Accepts Telegram voice messages
 • Converts speech to text
 • Returns recognized text to the user
 • Can be extended for NLP or emotion detection

🎵 2. Music Search (Deezer API)
 • Search tracks by:
   • Title
   • Artist
   • Genre
 • Returns:
   • Track name
   • Artist
   • Album
   • Cover image
   • Deezer link

⸻

🛠 Tech Stack
 • **Telegram Bot:** aiogram
 • **Backend API:** FastAPI
 • **Speech Recognition:** transform-model
 • **Music API:** Deezer Public API

⸻

📂 Project Structure

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
├── ai/
│   └── speech_recognition.py
│
├── resources/
│
├── requirements.txt
│
├── .env
│
├── README.md
│
└── .gitignore
```

⸻

🤖 Bot Commands

| Command | Description |
| :--- | :--- |
| `/start` | Start the bot |
| `/help` | Show help message |
| `/music` | Search for music |
| `Voice message` | Convert speech to text |

⸻

👥 Team Members
 • **Eric** – Telegram Bot & Deezer Integration
 • **Vlad** – AI / Voice Recognition

⸻

🗂 Task Distribution

### 1️⃣ Telegram Bot (aiogram)
**Assigned to:** Eric (Lead)
 • Bot command handling (`/start`, `/help`, `/music`)
 • Voice message handling
 • Message routing
 • Middleware
 • Integration with FastAPI
 • User session handling

**Support:** Vlad (testing & minor features)

⸻

### 2️⃣ FastAPI Backend
**Shared**

**Eric (Lead)**
 • Core FastAPI setup
 • API routes for bot integration
 • Deezer API service integration
 • Request validation
 • Error handling

**Vlad (Partial)**
 • Voice recognition endpoint
 • AI module integration
 • Logging

⸻

### 3️⃣ AI / Speech Recognition Module
**Assigned to:** Vlad (Lead)
 • Voice message processing
 • Speech-to-text integration
 • Text preprocessing
 • Future NLP expansion

**Support:** Eric (bot-side formatting & response handling)

⸻

### 4️⃣ Deezer API Integration
**Assigned to:** Eric (Lead)
 • Integration with Deezer Public API
 • Searching tracks by:
   • Title
   • Artist
   • Genre
 • Formatting music results for Telegram
 • Handling API limits & response parsing

**Support:** Vlad (optional improvements)

⸻

### 5️⃣ Testing & QA
**Shared**
 • FastAPI endpoint testing
 • Bot command testing
 • Voice recognition accuracy tests
 • End-to-end testing

⸻

🏗 Summary Table

| Task | Eric | Vlad |
| :--- | :---: | :---: |
| Telegram Bot | Lead | Support |
| FastAPI Core | Lead | Partial |
| Voice Recognition | Support | Lead |
| Deezer API | Lead | Support |
| Testing | Shared | Shared |
| Deployment | Shared | Shared |

⸻

📈 Future Improvements
 • Emotion detection from voice
 • Personalized recommendations
 • Caching layer (Redis)
 • Rate limiting
 • Admin panel
 • Web interface

⸻