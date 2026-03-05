from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

def mock_speech_to_text(audio_bytes: bytes) -> str:
    return "Распознано: Привет, как дела? Я — LSP, и у меня есть монетка."

@router.message(
    lambda m: m.voice is not None or m.video is not None or m.video_note is not None  
)
async def handle_media_for_stt(message: Message):
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
        file_bytes = await message.bot.download_file(file.file_path)

        recognized_text = mock_speech_to_text(file_bytes)

        await message.answer(
            recognized_text,
            parse_mode="HTML"
        )

    except Exception as e:
        await message.answer(f"❌ Error: {e}")
