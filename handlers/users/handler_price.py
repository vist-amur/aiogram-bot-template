import asyncio

import phonenumbers
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ChatActions

from loader import dp

from states import Price_steps
from utils.misc import get_addr1c
from handlers.users.menu import get_sales


@dp.message_handler(text='Узнать цену и наличие товара ₽')
async def price(message: types.Message, state: FSMContext):
    await message.answer(
        "Краткая инструкция для составления запроса по ценам и наличию товара: на следующем шаге "
        "укажите ключевые слова, через запятую, для поиска товара по наименованию, например: 'преч, "
        "дез, шапочк'")
    await Price_steps.prs_keywords.set()


@dp.message_handler(state=Price_steps.prs_keywords)
async def set_name(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == "Режим работы ⏰":
        await state.finish()
        await state.reset_state()
        return await message.answer(get_addr1c.get_clock_1c_brome())
    if answer == "Наш адрес 📨":
        await state.finish()
        await state.reset_state()
        return await message.answer(get_addr1c.get_addr1c_brome())
    if answer == 'Обратный звонок 📞':
        await state.finish()
        await state.reset_state()
        return await message.answer(get_addr1c.get_null())
    if answer == 'Задать вопрос 📢':
        await state.finish()
        await state.reset_state()
        return await message.answer(get_addr1c.get_null())
    if answer == 'Акции и скидки 📉':
        await state.finish()
        await state.reset_state()
        return await get_sales(message)
        #return await message.answer(get_addr1c.get_discounts_1c_brome())
    if answer == 'Наши реквизиты 📄':
        await state.finish()
        await state.reset_state()
        return await message.answer(get_addr1c.get_requisites_1c_brome())

    await dp.bot.send_message(message.chat.id, "обрабатываю запрос...")
    await asyncio.sleep(3)

    await state.update_data(answer_text=answer)

    user_data = await state.get_data()
    # get_addr1c.set_questions_1c_brome(user_data['answer_name'], user_data['answer_phone'], user_data['answer_text'])
    info = get_addr1c.get_price_1c_brome(user_data['answer_text'])
    if len(info) == 0:
        await message.answer('Товары не найдены! Измените запрос!')
        await state.finish()
        # await state.reset_state()
        return
    pOst = ""
    for i, y in enumerate(info):
        if y["Остаток"] == 0:
            pOst = "Нет в наличии ⭕"
        else:
            pOst = "В наличии ✅"
        istr = f'{y["Номенклатура"]}, Артикул: {y["Артикул"]}, {pOst}, Цена: {y["Цена"]} руб.'
        await message.answer(istr)

    await state.finish()
    # await state.reset_state()
