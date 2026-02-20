import asyncio
import logging

from aiogram.client.bot import DefaultBotProperties
from aiogram import Bot, Dispatcher

from config import config
from src.db.database import init_db
from src.bot.handlers import all_routers


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
)


async def main():
    init_db()
    
    bot = Bot(token=config.bot_token,
              default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher()

    for router in all_routers:
        dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
