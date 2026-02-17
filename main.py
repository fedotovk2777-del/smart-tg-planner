import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart
from datetime import datetime, timedelta
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import json

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет! Я твой AI планировщик 🧠\nНапиши: /plan 2h завтра")

@dp.message()
async def planner(message: Message):
    text = message.text.lower()

    if "2h" in text:
        duration = 2
    else:
        duration = 1

    start_time = datetime.now() + timedelta(hours=1)
    end_time = start_time + timedelta(hours=duration)

    await message.answer(
        f"Запланировал с {start_time.strftime('%H:%M')} до {end_time.strftime('%H:%M')}"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
