import os
from aiogram import Router, types
from dotenv import load_dotenv
import tempfile
import librosa
import torch

from transformers import WhisperForConditionalGeneration, WhisperProcessor

load_dotenv()

model = WhisperForConditionalGeneration.from_pretrained(
    os.getenv("MODEL_NAME")
)
processor = WhisperProcessor.from_pretrained(
    os.getenv("MODEL_NAME")
)

def speech_to_text_from_bytes_processor(audio_bytes: bytes) -> str:
    """
    Распознаёт речь через Processor + Model (Hugging Face)
    с пересэмплированием на 16kHz и автоопределением языка (русский/английский)
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_file.write(audio_bytes)
        temp_filename = tmp_file.name

    try:
        speech, sr = librosa.load(temp_filename, sr=16000)

        input_features = processor(speech, sampling_rate=16000, return_tensors="pt").input_features

        with torch.no_grad():
            short_ids = model.generate(
                input_features,
                task="transcribe",
                max_length=5
            )

        first_token = short_ids[0, 0].item()
        detected_token = processor.tokenizer.decode([first_token]).strip()

        lang_map = {
            "<|ru|>": "russian",
            "<|en|>": "english"
        }
        language = lang_map.get(detected_token, "russian")  
        print(f"🔍 Detected language token: {detected_token} → Using language: {language}")

        with torch.no_grad():
            predicted_ids = model.generate(
                input_features,
                language=language,
                task="transcribe",
                max_length=225
            )

        transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
        return transcription

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

    msg = await message.answer(f"📥 Received {media_type}. Processing...")

    try:
        file = await message.bot.get_file(file_id)
        file_bytes_io = await message.bot.download_file(file.file_path)
        file_bytes = file_bytes_io.read()

        recognized_text = speech_to_text_from_bytes_processor(file_bytes)

        await msg.edit_text(f"🗣️: {recognized_text}")

    except Exception as e:
        await msg.edit_text(f"❌ Error: {e}")