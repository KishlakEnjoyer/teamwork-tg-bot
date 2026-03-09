from aiogram import Router, types
from aiogram.filters import Command
from aiogram.filters.command import CommandObject
from dotenv import load_dotenv

import os
from openai import OpenAI

router = Router()

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL")

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=GROQ_API_KEY
)


def ask_model(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1024
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"GROQ API request failed: {e}"


@router.message(Command("ai"))
async def ai_command(message: types.Message, command: CommandObject):

    prompt = command.args

    if not prompt:
        await message.answer("Usage:\n/ai <text>")
        return

    msg = await message.answer("Thinking...")

    response = ask_model(prompt)

    await msg.edit_text(response)