from aiogram import types
from aiogram.filters import BaseFilter


class IsAdmin(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        return message.from_user.id == 123456789
