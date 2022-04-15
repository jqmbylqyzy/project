from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp
from keyboards.default import menu

@dp.message_handler(Command("start"))
async def show_menu(message:Message):
    await message.answer("Choose one", reply_markup = menu)

@dp.message_handler(Text(equals=["Dina", "Zhambylkyzy", "Mina", "Bombakyzy", "Kina", "Zhongarkyzy"]))
async def show_menu(message:Message):
    await message.answer(f"She is {message.text}.bye-bye", reply_markup = ReplyKeyboardRemove())

