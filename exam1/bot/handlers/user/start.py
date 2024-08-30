from aiogram.filters import CommandStart
from aiogram import types
from aiogram.types import Message
from aiogram.types import Message, InlineKeyboardMarkup
from aiogram import html
from keyboards.inline.menuKeyboard import menuButtons

from loader import dp, db

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    photo_url = 'https://img.freepik.com/premium-photo/neon-sign-that-says-name-store_999340-85372.jpg?ga=GA1.1.4029628.1724939545&semt=ais_hybrid'
    caption = """
    Telegram magazin botimizga xush kelibsiz!
    """
    await message.answer_photo(photo=photo_url, caption=caption, reply_markup=menuButtons)

    user_id = message.from_user.id
    user_name = message.from_user.full_name
    username = message.from_user.username
    phone_number = None  
    
    db.add_user(user_name, username, phone_number)