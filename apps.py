import asyncio
import logging
import sys

from aiogram import Bot
from aiogram.enums import ParseMode
from bot.dispatcher import TOKEN, dp



async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())















'''1) Birinchi ishlatiladigan komanda til fayl yaratadi'''
# 1) pybabel init -i locales/messages.pot -d locales -D messages -l en
# 1) pybabel init -i locales/messages.pot -d locales -D messages -l uz

'''2) extrack qilinadi py faylda nimadur ozgarsa komanda beriladi'''
# 2) pybabel extract -k _:1,1t -k _:1,2 -k __ --input-dirs=. -o locales/messages.pot


'''extrack dan keyin update shu komanda beriladi'''
# 3) pybabel update -d locales -D messages -i locales/messages.pot


'''oxirida kompayl ishga tushish uchun'''
# 4) pybabel compile -d locales -D messages