import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher

from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('TOKEN')


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
