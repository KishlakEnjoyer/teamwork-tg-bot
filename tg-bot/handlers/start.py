from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart

from keyboards import keyboard_contacts

router = Router()

@router.message(CommandStart())
async def send_welcome(message: types.Message):
    """
    Just a welcome message with some instructions and a contact keyboard.
    """
    await message.answer(f'Hi,{message.from_user.first_name}!' +
            '\nThis is a bot for recognition your voice and video messages!' +
            '\nAlso you can search music! Just try command /music' +
            '\nContacts of the developers ⬇️', reply_markup=keyboard_contacts.contacts)
    
@router.message(Command("help"))
async def send_welcome(message: types.Message):
    """
    Help message showing available commands and features.
    """
    help_text = (
        f"👋 Hi, {message.from_user.first_name}!\n\n"
        "<b>Available Commands:</b>\n"
        "/start - Start the bot and see the welcome message\n"
        "/help - Show this help message\n"
        "/music &lt;text&gt; - Search for music tracks (e.g., /music monetka)\n"
        "/emotion &lt;text&gt; - Analyze the sentiment of the provided text (e.g., /emotion I am happy)\n\n"
        "<b>Other Features:</b>\n"
        "Send a <b>voice message</b> or <b>video note</b> (round video) to have the speech recognized automatically."
    )
    await message.answer(help_text, reply_markup=keyboard_contacts.contacts, parse_mode="HTML")