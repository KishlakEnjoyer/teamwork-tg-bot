from aiogram.fsm.state import State, StatesGroup

class MusicSearchState(StatesGroup):
    """
    State for music search. User will be asked to send a name of the song or artist.
    """
    waiting_for_music_name = State()