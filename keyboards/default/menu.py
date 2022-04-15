from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Dina"),
            KeyboardButton(text="Zhambylkyzy")
        ],
        [
            KeyboardButton(text="Mina"),
            KeyboardButton(text="Bombakyzy")
        ],
        [
            KeyboardButton(text="Kina"),
            KeyboardButton(text="Zhongarkyzy")
        ],
    ],
    resize_keyboard=True
)