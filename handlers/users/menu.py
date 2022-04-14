from aiogram import types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.dispatcher.filters import Command
from keyboards.default import menu
from loader import dp
from utils.misc import get_addr1c
import asyncio


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer('Главное меню', reply_markup=menu)


@dp.message_handler(text='Наш адрес 📨')
async def get_addr1ch(message: types.Message):
    await dp.bot.send_message(message.chat.id, "обрабатываю запрос...")
    await asyncio.sleep(3)
    await message.answer(get_addr1c.get_addr1c_brome())


@dp.message_handler(text='Режим работы ⏰')
async def get_addr1ch(message: types.Message):
    await dp.bot.send_message(message.chat.id, "обрабатываю запрос...")
    await asyncio.sleep(3)
    await message.answer(get_addr1c.get_clock_1c_brome())


@dp.message_handler(text='Наши реквизиты 📄')
async def get_addr1ch(message: types.Message):
    await dp.bot.send_message(message.chat.id, "обрабатываю запрос...")
    await asyncio.sleep(3)
    info = get_addr1c.get_requisites_1c_brome()

    await message.answer(info.replace("*", "\r\n"))

@dp.message_handler(text='Акции и скидки 📉')
async def get_sales(message: types.Message):
    await dp.bot.send_message(message.chat.id, "обрабатываю запрос...")
    await asyncio.sleep(3)
    info = get_addr1c.get_discounts_1c_brome()
    if len(info) == 0:
        await message.answer('Действующие акции не найдены!')
        return
    for i, y in enumerate(info):
        istr = f'{y["Номенклатура"]}, Артикул: {y["Артикул"]}, Старая цена: {y["Старая цена"]}, Новая цена: {y["Новая цена"]},' \
               f'Дата окончания акции: {y["Дата окончания акции"]}'
        await message.answer(istr)

