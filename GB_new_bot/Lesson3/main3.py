import asyncio
import config3
from aiogram import Bot, Dispatcher, types, F
import logging
from handlers import common, career_choice


async def main():
     # Включаем логгирование
     logging.basicConfig(level=logging.INFO)

     # Создаем объект бота
     bot = Bot(token=config3.token)

     # Диспечер
     dp = Dispatcher()

     dp.include_router(career_choice.router)
     dp.include_router(common.router)

     await dp.start_polling(bot)

if __name__ == '__main__':
     asyncio.run(main())
