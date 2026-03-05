import whisper
import tempfile
import os
import io  
from aiogram import Router, types

model = whisper.load_model("small")

def speech_to_text_from_bytes(audio_bytes: bytes) -> str:
    """
    Принимает аудио в виде bytes (например, из bot.download_file),
    возвращает распознанный текст.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".ogg") as tmp_file:
        tmp_file.write(audio_bytes)
        temp_filename = tmp_file.name

    try:
        result = model.transcribe(temp_filename)
        return result["text"]
    finally:
        os.unlink(temp_filename)

router = Router()

@router.message(
    lambda m: not m.text.startswith('/') if m.text else True,  
    lambda m: m.voice is not None or m.video is not None or m.video_note is not None  
)
async def handle_media_for_stt(message: types.Message):
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

    await message.answer(f"Get {media_type}. Loading...")

    try:
        file = await message.bot.get_file(file_id)
        file_bytes_io = await message.bot.download_file(file.file_path)
        
        file_bytes = file_bytes_io.read()

        recognized_text = speech_to_text_from_bytes(file_bytes)

        await message.answer(
            f"🗣️: {recognized_text}"
        )

    except Exception as e:
        await message.answer(f"❌ Error: {e}")