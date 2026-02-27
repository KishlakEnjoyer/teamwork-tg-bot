# Virtual environment
python -m venv venv 
venv\Scripts\activate
pip freeze > requirements.txt

# Core
pip install fastapi uvicorn[standard] pydantic python-dotenv

# Telegram Bot
pip install aiogram

# Database
# PostgreSQL
pip install asyncpg sqlalchemy databases
# MySQL
pip install mysqlclient sqlalchemy databases

# AI / ML
pip install torch transformers

# HTTP requests / API
pip install httpx spotipy

# Optional for analytics / utils
pip install scikit-learn matplotlib

# API Launch
uvicorn main:app --reload