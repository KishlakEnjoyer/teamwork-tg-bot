# 👥 Team Members

* **[Erik](https://github.com/KishlakEnjoyer)**
* **[Vlad](https://github.com/N0Nameez)** 

---

# 🗂 Task Distribution

## 1. Telegram Bot (aiogram)

**Assigned to: Eric (Lead)**

* Bot command handling (`/start`, `/help`, `/music`, `/analyze`, `/profile`)
* Message routing and middleware
* Integrating bot with FastAPI endpoints
* Handling session/user state

**Support:** Vlad can help with testing or minor command additions

---

## 2. FastAPI Backend

**Assigned: Shared**

* **Eric (Main focus)**

  * Setting up core FastAPI structure
  * Creating API endpoints for Telegram bot integration
  * Handling user requests and responses
  * API authentication / configuration
  * Connecting backend with database

* **Vlad (Partial)**

  * Writing endpoints for AI services (`/analyze`, `/music`)
  * Handling AI module calls from FastAPI
  * Implementing logging and error handling

---

## 3. Database (PostgreSQL)

**Assigned to: Vlad (Lead)**

* Designing database schema: users, messages, personality_profile, music_history
* Creating tables and relations using SQLAlchemy
* Writing async database queries using asyncpg
* Handling database migrations

**Support:** Eric assists in connecting endpoints to the database

---

## 4. AI / ML Module

**Assigned to: Vlad (Lead)**

* Emotion detection with `j-hartmann/emotion-multilingual-distilroberta-base`
* Personality profile building logic
* Mapping emotions → music genres
* Preparing dataset for future training or analytics

**Support:** Eric can integrate the AI responses into bot messages

---

## 5. Music API Integration (Spotify)

**Assigned to: Eric (Lead)**

* Integrating Spotify Web API via `spotipy`
* Searching tracks and playlists
* Sending recommended music to FastAPI / Telegram Bot
* Handling API keys and authorization

**Support:** Vlad can help map AI emotion output to Spotify genres

---

## 6. Testing & QA

**Shared:**

* Unit tests for FastAPI endpoints (both)
* Telegram bot testing (Eric lead)
* AI module accuracy checks (Vlad lead)
* End-to-end integration testing

---

## 7. DevOps / Deployment

**Shared:**

* Docker setup (optional)
* Environment variables and secrets management
* VPS deployment (EU recommended for Spotify API)

---

# 🏗 Summary Table

| Task           | Eric    | Vlad    |
| -------------- | ------- | ------- |
| Telegram Bot   | Lead    | Support |
| FastAPI Core   | Lead    | Partial |
| Database       | Support | Lead    |
| AI / ML Module | Support | Lead    |
| Music API      | Lead    | Support |
| Testing        | Shared  | Shared  |
| Deployment     | Shared  | Shared  |

---

This way:

* **Eric focuses on what he’s strongest at** (bot + FastAPI core + Spotify)
* **Vlad focuses on AI and database** but still contributes to FastAPI
* Both share testing and deployment for full integration

---


