from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup
from aiogram import html
from keyboards.inline.menuKeyboard import menuButtons
# from keyboards.inline.productsInline import ovqatlarButton

from loader import dp, db

@dp.message(lambda message: message.text == "🍔Burger")
async def kurslar_handlers(message: Message):
    photo_url = 'https://img.freepik.com/free-photo/tasty-burger-isolated-white-background-fresh-hamburger-fastfood-with-beef-cheese_90220-1063.jpg?ga=GA1.1.4029628.1724939545&semt=ais_hybrid'
    price = 32990
    my_laptop = f"""
     🍔Burger
    Narxi: {price} so'm
    Mazali va birinchi luqmadan ko'proq burger yeyishni xohlaysiz😋"""
    await message.answer_photo(photo=photo_url, caption=my_laptop)

@dp.message(lambda message: message.text == "🍕Pizza")
async def kurslar_handlers(message: Message):
    photo_url = 'https://img.freepik.com/free-photo/beef-mushroom-pizza-with-onion-cheese-wooden-plate_140725-10431.jpg?ga=GA1.1.4029628.1724939545&semt=ais_hybrid'
    price = 81990
    my_laptop = f"""
     🍕Pizza
    Narxi: {price} so'm"""
    await message.answer_photo(photo=photo_url, caption=my_laptop)

@dp.message(lambda message: message.text == "🥘Lavash")
async def kurslar_handlers(message: Message):
    photo_url = 'https://img.freepik.com/premium-photo/two-slices-pizza-are-table-one-which-has-fire-coming-out-it_976492-70718.jpg?ga=GA1.1.4029628.1724939545&semt=ais_hybrid'
    price = 27490
    my_laptop = f"""
     🥘Lavash
    Narxi: {price} so'm
   Lavash nonini guruh sifatida pishirish oila, jamiyat va ijtimoiy munosabatlarni mustahkamlaydi.Odatda mahalliy pishloqlar va o'tlarga o'ralgan holda xizmat qiladi va muzlatgichda oltioygacha saqlanishi mumkin."""
    await message.answer_photo(photo=photo_url, caption=my_laptop)

#☕Coffee
@dp.message(lambda message: message.text == "☕Coffee")
async def kurslar_handlers(message: Message):
    photo_url = 'https://img.freepik.com/free-photo/fresh-coffee-steams-wooden-table-close-up-generative-ai_188544-8923.jpg?ga=GA1.1.4029628.1724939545&semt=ais_hybrid'
    price = 15490
    my_laptop = f"""
    ☕Coffee
    Narxi: {price} so'm
    Coffee - bu sizning energiyangizni oshiradigan eng yaxshi ichimliklardan biri. Sizga qulay va qiziqarli dam olish uchun kofe ichish kerak"""
    await message.answer_photo(photo=photo_url, caption=my_laptop)

@dp.message(lambda message: message.text == "🍴Menu")
async def kurslar_handlers(message: Message):
    await message.answer("Menuga hush kelibsiz", reply_markup=menuButtons)