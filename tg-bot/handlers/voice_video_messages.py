import os
import subprocess
import tempfile
import librosa
import torch
from aiogram import Router, types, F
from aiogram.filters import Command
from dotenv import load_dotenv
from transformers import WhisperForConditionalGeneration, WhisperProcessor
from keyboards import keyboard_languages

load_dotenv()

model = WhisperForConditionalGeneration.from_pretrained(os.getenv("MODEL_NAME"))
processor = WhisperProcessor.from_pretrained(os.getenv("MODEL_NAME"))

user_languages: dict[int, str] = {}


def get_user_language(user_id: int) -> str:
    """Returns the language set by the user, defaults to English."""
    return user_languages.get(user_id, "english")


def speech_to_text_from_bytes_processor(audio_bytes: bytes, language: str, suffix: str = ".ogg") -> str:
    """Transcribes audio bytes to text using Whisper model with the given language."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
        tmp_file.write(audio_bytes)
        temp_input = tmp_file.name

    temp_wav = temp_input.rsplit(".", 1)[0] + ".wav"

    try:
        subprocess.run(
            ["ffmpeg", "-y", "-i", temp_input, "-ar", "16000", "-ac", "1", temp_wav],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        speech, sr = librosa.load(temp_wav, sr=16000)
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
        os.unlink(temp_input)
        if os.path.exists(temp_wav):
            os.unlink(temp_wav)


router = Router()


@router.message(Command("lang"))
async def cmd_lang(message: types.Message):
    """Handles /lang command and sends language selection keyboard."""
    current_lang = get_user_language(message.from_user.id)
    await message.answer(
        "Select language for speech recognition:",
        reply_markup=keyboard_languages.build_lang_keyboard(current_lang)
    )


@router.callback_query(F.data.startswith("lang_"))
async def callback_lang(callback: types.CallbackQuery):
    """Handles language selection callback and updates user language preference."""
    user_id = callback.from_user.id
    language = callback.data.replace("lang_", "")
    user_languages[user_id] = language

    await callback.message.edit_reply_markup(reply_markup=keyboard_languages.build_lang_keyboard(language))
    lang_label = "🇷🇺 Русский" if language == "russian" else "🇬🇧 English"
    await callback.answer(f"Language set to {lang_label}")


@router.message(F.voice | F.video | F.video_note)
async def handle_media_for_stt(message: types.Message):
    """Handles incoming voice, video and video note messages and runs speech recognition."""
    file_id = None
    suffix = ".ogg"

    if message.voice:
        file_id = message.voice.file_id
        suffix = ".ogg"
    elif message.video:
        file_id = message.video.file_id
        suffix = ".mp4"
    elif message.video_note:
        file_id = message.video_note.file_id
        suffix = ".mp4"

    language = get_user_language(message.from_user.id)
    msg = await message.answer("📥 Processing...")

    try:
        file = await message.bot.get_file(file_id)
        file_bytes_io = await message.bot.download_file(file.file_path)
        file_bytes = file_bytes_io.read()

        recognized_text = speech_to_text_from_bytes_processor(file_bytes, language, suffix)
        flag = "🇷🇺" if language == "russian" else "🇬🇧"
        await msg.edit_text(f"🗣️{flag}: {recognized_text}")

    except Exception as e:
        await msg.edit_text(f"❌ Error: {e}")