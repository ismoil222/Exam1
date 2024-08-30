from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menuButtons = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="😋Mahsulotlar"),    
            KeyboardButton(text="🤖Shaxsiy kabinet")
        ],
        [
            KeyboardButton(text="💻Men haqimda"),
            KeyboardButton(text="🍴Menu")
        ]
    ]
)