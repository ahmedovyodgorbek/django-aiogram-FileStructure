from aiogram import types, Router, F
from aiogram.filters.command import CommandStart

class StartHandler:
    def __init__(self):
        self.router = Router()
        self.register_handlers()

    def register_handlers(self):
        # 1
        self.router.message(CommandStart())(self.start)
        self.router.message(F.text.lower() == 'hello', F.chat.type == 'private')(self.hello)
        self.router.message(F.text.contains('hi'))(self.welcome)

    async def start(self, message: types.Message):
        await message.answer("👋 Welcome! I'm your bot.")

    async def welcome(self, message: types.Message):
        await message.answer("👋 hi")

    async def hello(self, message: types.Message):
        await message.answer("👋 Hello")
