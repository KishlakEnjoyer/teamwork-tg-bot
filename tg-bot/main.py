import asyncio
import logging
import threading
import os
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from dotenv import load_dotenv 

from handlers import start, music, voice_video_messages

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

dp.include_router(start.router)
dp.include_router(music.router)
dp.include_router(voice_video_messages.router)

async def main():
    commands = [
        BotCommand(command="start", description="Main menu"),
        BotCommand(command="music", description="Music action"),
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