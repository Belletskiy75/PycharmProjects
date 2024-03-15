import asyncio
import config
import aiogram
from aiogram.filters.command import Command
import logging
import random

#Включаем логгирование
logging.basicConfig(level=logging.INFO)

#Создаем объект бота
bot = aiogram.Bot(token=config.token)

#Диспечер
dp = aiogram.Dispatcher()


#Хэндлер на команду /start
@dp.message(Command('start'))
async def cmd_start(message: aiogram.types.Message):
     name = message.chat.first_name
     await message.answer(f'Привет, {name}')


#Хэндлер на команду /stop
@dp.message(Command('stop'))
async def cmd_stop(message: aiogram.types.Message):
     name = message.chat.first_name
     await message.answer(f'Пока, {name}')


#Хэндлер на команду /work
@dp.message(Command('work'))
async def cmd_stop(message: aiogram.types.Message):
     name = message.chat.first_name
     await message.answer(f'Хорошо, {name}')

#Хэндлер на команду /health
@dp.message(Command('health'))
async def cmd_stop(message: aiogram.types.Message):
     name = message.chat.first_name
     await message.answer(f'Пыхтим потихоньку, {name}')
async def main():
     await dp.start_polling(bot)


if __name__ == '__main__':
     asyncio.run(main())
