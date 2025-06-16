import asyncio
import logging
import os
import sys

import django
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from bot.handlers.start import StartHandler
from load_env import TOKEN


async def main():

    bot = Bot(token=TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    await bot.delete_webhook(drop_pending_updates=True)

    # Initialize handlers (registers routes to routers)
    start_handler = StartHandler()

    # Add routers to dispatcher
    dp.include_router(router=start_handler.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
