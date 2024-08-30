from aiogram import F
from aiogram.types import Message
from loader import dp, db, bot
import sqlite3
from data.config import ADMINS


@dp.message(F.text == '🤖Shaxsiy kabinet')
async def personal_combinet(message: Message) -> None:
    name = message.from_user.full_name
    await bot.send_message(
        chat_id=ADMINS[0],
        text=f"Sizning ismingiz: {name}\nID: {message.from_user.id}\nUsername: @{message.from_user.username} "
    )
