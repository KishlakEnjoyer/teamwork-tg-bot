from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext


from keyboards import keyboard_back, keyboard_contacts
from states.state_music_search_state import MusicSearchState

router = Router()

@router.message(Command("music"))
async def music(message: types.Message, state: FSMContext):
    """
    Handler for the /music command. Just a message with some instructions and a back button.
    """
    await message.answer('Here you can search music! Just send me the name of the song or the artist!', reply_markup=keyboard_back.back)
    await state.set_state(MusicSearchState.waiting_for_music_name)
    await message.answer()

@router.callback_query(F.data == 'back')
async def back_to_main_menu(callback_query: types.CallbackQuery, state: FSMContext):
    """
    Handler for the back button. Just a message with some instructions and a contact keyboard.
    """
    await callback_query.message.edit_text(f'Hi,{callback_query.from_user.first_name}!' +
            '\nThis is a bot for recognition your voice and video messages!' +
            '\nAlso you can search music! Just try command /music' +
            '\nContacts of the developers ⬇️', reply_markup=keyboard_contacts.contacts)
    await state.set_state(MusicSearchState.waiting_for_music_name)
    await callback_query.answer()
    
