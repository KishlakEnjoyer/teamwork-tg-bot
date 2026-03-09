import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from dotenv import load_dotenv 

from handlers import start, music, voice_video_messages, emotion_analysis, ai_chat

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

dp.include_router(start.router)
dp.include_router(music.router)
dp.include_router(voice_video_messages.router)
dp.include_router(emotion_analysis.router)
dp.include_router(ai_chat.router)

async def main():
    commands = [
        BotCommand(command="start", description="Just a welcome message with some instructions and a contact keyboard."),
        BotCommand(command="music", description="Music action"),
        BotCommand(command="help", description="Help message showing available commands and features."),
        BotCommand(command="emotion", description="Analyze the sentiment of the provided text. Usage: /emotion Your text here"),
        BotCommand(command="ai", description="Ask the AI a question.")
    ]
    await bot.set_my_commands(commands)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    print('Bot running!')
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stopped!')