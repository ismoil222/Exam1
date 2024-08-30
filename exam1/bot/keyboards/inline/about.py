from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_info():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="💬 Мой лc", url="https://t.me/wakeup999_noo"),
            ],
            [
                InlineKeyboardButton(text="Мой GitHub", url="https://github.com/ismoil222"),
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return keyboard