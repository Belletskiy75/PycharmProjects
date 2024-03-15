import asyncio
import config2
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import logging
import random
from keyboards import kb1, kb2
from random_fox import fox

#Включаем логгирование
logging.basicConfig(level=logging.INFO)

#Создаем объект бота
bot = Bot(token=config2.token)

#Диспечер
dp = Dispatcher()


#Хэндлер на команду /start
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
     name = message.chat.first_name
     await message.answer(f'Привет, {name}', reply_markup=kb1)

#Хэндлер на команду /fox
@dp.message(Command('fox'))
@dp.message(Command('лиса'))
@dp.message(F.text.lower() == 'покажи лису')
async def cmd_fox(message: types.Message):
     name = message.chat.first_name
     img_fox = fox()
     await message.answer(f'Держи лису, {name}')
     await message.answer_photo(photo=img_fox)
     # await bot.send_photo(message.from_user.id, photo=img_fox)

#Хэндлер на команду /work
@dp.message(Command('work'))
async def cmd_stop(message: types.Message):
     name = message.chat.first_name
     await message.answer(f'Хорошо, {name}')

#Хэндлер на команду /health
@dp.message(Command('health'))
async def cmd_stop(message: types.Message):
     name = message.chat.first_name
     await message.answer(f'Пыхтим потихоньку, {name}')

#Хендлер на сообщения
@dp.message(F.text)
async def msg_echo(message: types.Message):
     msg_user = message.text.lower()
     name = message.chat.first_name
     if 'привет' in msg_user:
          await message.answer(f'Привет-привет, {name}')
     elif 'пока' == msg_user:
          await message.answer(f'Пока-пока, {name}')
     elif 'ты кто' in msg_user:
          await message.answer_dice(emoji="🎲")
     else:
          await message.answer(f'Я не знаю такого слова')

async def main():
     await dp.start_polling(bot)


if __name__ == '__main__':
     asyncio.run(main())
