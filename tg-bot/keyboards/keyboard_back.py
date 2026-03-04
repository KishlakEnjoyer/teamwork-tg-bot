from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🔙 Назад', callback_data='back')]
])