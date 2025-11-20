

BOT_TOKEN = ""

import asyncio
import logging
from RateLimitMiddleware import RateLimitMiddleware
import json

from aiogram.client.default import DefaultBotProperties
# import config
from aiogram import Bot
from aiogram import Dispatcher
from aiogram.enums import ParseMode
from routers import router as main_router

async def main():
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )
    dp = Dispatcher()
    dp.include_routers(main_router)
    dp.message.middleware(RateLimitMiddleware(limit=3))
    logging.basicConfig(level=logging.DEBUG)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())