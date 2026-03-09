from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def build_lang_keyboard(current_lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🇷🇺 Русский" + (" ✅" if current_lang == "russian" else ""),
                callback_data="lang_russian"
            ),
            InlineKeyboardButton(
                text="🇬🇧 English" + (" ✅" if current_lang == "english" else ""),
                callback_data="lang_english"
            ),
        ]
    ])