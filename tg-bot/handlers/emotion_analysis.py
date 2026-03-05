from aiogram import Router, F, types
from aiogram.filters import Command
from transformers import pipeline

router = Router()

# Load the model once when the bot starts
sentiment_analyzer = pipeline(
    "text-classification",
    model="tabularisai/multilingual-sentiment-analysis",
    top_k=1  
)

@router.message(Command('emotion'))
async def analyze_sentiment(message: types.Message):
    command_text = message.text.split(maxsplit=1)
    if len(command_text) < 2:
        await message.answer("Please provide text after /emotion.\nExample: /emotion This is a great day!")
        return

    text = command_text[1]  # Get the part after '/emotion'

    try:
        result = sentiment_analyzer(text)

        if isinstance(result, list) and len(result) > 0:
            first_item = result[0]
            if isinstance(first_item, list) and len(first_item) > 0:
                actual_result = first_item[0]
            elif isinstance(first_item, dict):
                actual_result = first_item
            else:
                await message.answer("❌ Error: Unexpected model output structure.")
                return
        else:
            await message.answer("❌ Error: Model returned no results.")
            return

        label = actual_result.get('label', 'Unknown')
        confidence = actual_result.get('score', 0.0)

        emoji_map = {
            'Very Positive': '🥰',
            'Positive': '😊',
            'Neutral': '😐',
            'Negative': '😞',
            'Very Negative': '😡'
        }

        emoji = emoji_map.get(label, '❓')

        await message.answer(
            f"💬 Text: <i>{text}</i>\n"
            f"📈 Sentiment: {emoji} <b>{label}</b> ({confidence:.2f})",
            parse_mode="HTML"
        )

    except Exception as e:
        await message.answer(f"❌ Error processing sentiment: {e}")