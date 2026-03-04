from fastapi import FastAPI
import requests as rq
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL_API")

app = FastAPI(
    title="SpeechMusicBot - API",
    description="API for TG Speech and Music Bot by Erik&Vladislav"
)

@app.get("/get_track")
def get_track_by_title_or_singer(text: str):
    """
    Method for getting info of track by request
    """
    response = rq.get(
        f"{BASE_URL}/search",
        params={"q": text, "limit": 3}
    )

    if response.status_code != 200:
        return {
            "message": "Deezer API error",
            "errorCode": response.status_code
        }

    data = response.json()

    if not data["data"]:
        return {
            "message": "Track not found",
            "errorCode": 404
        }

    tracks = []
    for track in data["data"]:
        tracks.append({
            "title": track["title"],
            "artist": track["artist"]["name"],
            "album": track["album"]["title"],
            "preview": track["preview"],
            "link": track["link"],
            "image": track["picture_xl"]
        })

    return {
        "message": "Track was successfully found!",
        "errorCode": 200,
        "tracks": tracks
    }