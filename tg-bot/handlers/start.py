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