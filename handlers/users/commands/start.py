from aiogram import types

from loader import dp


@dp.message_handler(chat_type='private', commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет, я бот!')