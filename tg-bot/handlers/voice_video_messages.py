import os
from aiogram import Router, types, F
from aiogram.filters import Command
from dotenv import load_dotenv
import tempfile
import librosa
import torch
from transformers import WhisperForConditionalGeneration, WhisperProcessor
from keyboards import keyboard_languages

load_dotenv()

model = WhisperForConditionalGeneration.from_pretrained(os.getenv("MODEL_NAME"))
processor = WhisperProcessor.from_pretrained(os.getenv("MODEL_NAME"))

user_languages: dict[int, str] = {}


def get_user_language(user_id: int) -> str:
    """
    Returns the language set by the user, defaults to English.
    """
    return user_languages.get(user_id, "english")


def speech_to_text_from_bytes_processor(audio_bytes: bytes, language: str) -> str:
    """
    Transcribes audio bytes to text using Whisper model with the given language.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_file.write(audio_bytes)
        temp_filename = tmp_file.name

    try:
        speech, sr = librosa.load(temp_filename, sr=16000)
        input_features = processor(speech, sampling_rate=16000, return_tensors="pt").input_features

        with torch.no_grad():
            predicted_ids = model.generate(
                input_features,
                language=language,
                task="transcribe",
                max_new_tokens=225
            )

        return processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]

    finally:
        os.unlink(temp_filename)


router = Router()


@router.message(Command("lang"))
async def cmd_lang(message: types.Message):
    """
    Handles /lang command and sends language selection keyboard.
    """
    current_lang = get_user_language(message.from_user.id)
    await message.answer(
        "Select language for speech recognition:",
        reply_markup=keyboard_languages.build_lang_keyboard(current_lang)
    )


@router.callback_query(F.data.startswith("lang_"))
async def callback_lang(callback: types.CallbackQuery):
    """
    Handles language selection callback and updates user language preference.
    """
    user_id = callback.from_user.id
    language = callback.data.replace("lang_", "")
    user_languages[user_id] = language

    await callback.message.edit_reply_markup(reply_markup=keyboard_languages.build_lang_keyboard(language))
    lang_label = "🇷🇺 Русский" if language == "russian" else "🇬🇧 English"
    await callback.answer(f"Language set to {lang_label}")


@router.message(
    lambda m: not m.text.startswith('/') if m.text else True,
    lambda m: m.voice is not None or m.video is not None or m.video_note is not None
)
async def handle_media_for_stt(message: types.Message):
    """
    Handles incoming voice, video and video note messages and runs speech recognition.
    It detects the media type, retrieves the file, processes it with Whisper model and sends back the recognized text.
    """
    media_type = None
    file_id = None

    if message.voice:
        media_type = "voice"
        file_id = message.voice.file_id
    elif message.video:
        media_type = "video"
        file_id = message.video.file_id
    elif message.video_note:
        media_type = "video_note"
        file_id = message.video_note.file_id

    language = get_user_language(message.from_user.id)
    msg = await message.answer(f"📥 Received {media_type}. Processing...")

    try:
        file = await message.bot.get_file(file_id)
        file_bytes_io = await message.bot.download_file(file.file_path)
        file_bytes = file_bytes_io.read()

        recognized_text = speech_to_text_from_bytes_processor(file_bytes, language)
        flag = "🇷🇺" if language == "russian" else "🇬🇧"
        await msg.edit_text(f"🗣️{flag}: {recognized_text}")

    except Exception as e:
        await msg.edit_text(f"❌ Error: {e}")