from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

ovqatlarButton = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="🍔Burger"),    
            KeyboardButton(text="🍕Pizza")
        ],
        [
            KeyboardButton(text="🥘Lavash"),
            KeyboardButton(text="☕Coffee")
        ],
        [
            KeyboardButton(text="🍴Menu")
        ]
    ]
)
