from aiogram.filters import CommandStart
from aiogram import types, F
from aiogram.types import Message, InlineKeyboardMarkup
from aiogram import html
from keyboards.inline.about import get_info
from keyboards.inline.menuKeyboard import menuButtons
from keyboards.inline.productsInline import ovqatlarButton

from loader import dp, db

@dp.message(lambda message: message.text == "😋Mahsulotlar")
async def kurslar_handlers(message: Message):
    await message.answer("Kerakli ovqatni tanlang", reply_markup=ovqatlarButton)


@dp.message(F.text == '💻Men haqimda')
async def show_info(message: Message) -> None:
    info_keyboard = get_info()
    await message.answer('Men haqimdagi qisqacha saytlar:', reply_markup=info_keyboard)

@dp.message(lambda message: message.text == "🍴Menu")
async def kurslar_handlers(message: Message):
    await message.answer("Menuga hush kelibsiz", reply_markup=menuButtons)