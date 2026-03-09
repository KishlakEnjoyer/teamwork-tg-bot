from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart

from keyboards import keyboard_contacts

router = Router()

@router.message(CommandStart())
async def send_welcome(message: types.Message):
    """
    Just a welcome message with some instructions and a contact keyboard.
    """
    await message.answer(
        f"🎉 <b>Welcome, {message.from_user.first_name}!</b>\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "🎙 <b>Speech Recognition</b>\n"
        "    <i>Send a voice message, video or\n"
        "    🔵 round note — I'll transcribe it!</i>\n\n"
        "🎵 <b>Music Search</b>\n"
        "    <i>Use /music to find any track</i>\n\n"
        "🧠 <b>AI Assistant</b>\n"
        "    <i>Use /ai to ask me anything</i>\n\n"
        "❓ <b>Any questions left?</b>\n"
        "    <i>Use /help to see all available commands</i>\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "📬 <b>Contact the developers:</b>",
        reply_markup=keyboard_contacts.contacts,
        parse_mode="HTML"
    )
    
@router.message(Command("help"))
async def send_welcome(message: types.Message):
    """
    Help message showing available commands and features.
    """
    help_text = (
        f"👋 <b>Hey, {message.from_user.first_name}!</b>\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "🤖 <b>Commands</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "🚀 /start — Welcome message\n"
        "❓ /help — Show this menu\n\n"
        "🎵 /music <code>&lt;text&gt;</code>\n"
        "    <i>Search for music tracks</i>\n\n"
        "💬 /emotion <code>&lt;text&gt;</code>\n"
        "    <i>Analyze sentiment of text</i>\n\n"
        "🧠 /ai <code>&lt;text&gt;</code>\n"
        "    <i>Ask the AI anything</i>\n\n"
        "🌐 /lang — Set recognition language\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "🎙 <b>Voice & Video</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Send a <b>voice message</b>, <b>video</b> or\n"
        "🔵 <b>round video note</b> — and I'll\n"
        "automatically convert speech to text!\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "💡 <i>Tip: use /lang to switch between\n"
        "🇷🇺 Russian and 🇬🇧 English</i>"
    )
    await message.answer(help_text, reply_markup=keyboard_contacts.contacts, parse_mode="HTML")