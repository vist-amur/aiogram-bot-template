from aiogram import types


from loader import dp
from filters import isAddr
from utils.misc import get_addr1c

@dp.message_handler(isAddr(), text='/addr')
async def bot_test(message: types.Message):
    await message.answer(get_addr1c.get_addr1c_brome())
