from aiogram.dispatcher.filters import BoundFilter
from aiogram import types


class isAddr(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.text == '/addr'