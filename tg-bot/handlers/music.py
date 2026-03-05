from aiogram import Router, types
from aiogram.filters import Command
from aiogram.filters.command import CommandObject
from aiogram.types import InputMediaPhoto, InputMediaAudio, BufferedInputFile
import requests as rq
import os
from dotenv import load_dotenv

router = Router()
load_dotenv()
BASE_URL_FASTAPI = os.getenv("BASE_URL_FASTAPI")


@router.message(Command("music"))
async def music(message: types.Message, command: CommandObject):
    """
    Handles the /music command, searches for tracks via an API, sends image thumbnails with captions,
    and sends audio previews as a media group.
    """
    if not command.args:
        await message.answer("Usage:\n/music <track or artist>")
        return

    text = command.args

    response = rq.get(f"{BASE_URL_FASTAPI}/get_track", params={"text": text})
    if response.status_code != 200:
        await message.answer("API error")
        return

    data = response.json()
    tracks = data.get("tracks", [])
    if not tracks:
        await message.answer("Track not found")
        return

    caption_text = "\n".join(
        [f'{i+1}.{t["title"]}({t["album"]}) — {t["artist"]}\nFull: {t["link"]}' for i, t in enumerate(tracks)]
    )

    media_photos = []
    for i, track in enumerate(tracks[:3]):
        media_photos.append(InputMediaPhoto(
            media=track["image"],
            caption=caption_text if i == 0 else None  
        ))

    await message.answer_media_group(media_photos)

    media_audio = []
    for track in tracks:
        audio_resp = rq.get(track["preview"])
        audio_file = BufferedInputFile(audio_resp.content, filename=f"{track['title']} - {track['artist']}.mp3")
        media_audio.append(InputMediaAudio(media=audio_file, title=track['title'], performer=track['artist']))

    await message.answer_media_group(media_audio)