import phonenumbers
from aiogram import types
from aiogram.dispatcher import FSMContext
from phonenumbers import NumberParseException

from loader import dp

from states import Questions_steps
from handlers.users.menu import get_sales
from utils.misc import get_addr1c
from utils.misc import mail


@dp.message_handler(text='Задать вопрос 📢')
async def qwst_name(message: types.Message):
    await message.answer(
        "Как к Вам можно обращаться?")
    await Questions_steps.qwst_name.set()


@dp.message_handler(state=Questions_steps.qwst_name)
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
    if answer == 'Узнать цену и наличие товара ₽':
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

    await state.update_data(answer_name=answer)

    await message.answer(
        "Пожалуйста укажите Ваш номер телефона.")
    await Questions_steps.qwst_phone.set()


@dp.message_handler(state=Questions_steps.qwst_phone)
async def set_phone(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer_phone=answer)

    user_data = await state.get_data()
    try:
        mynumber = phonenumbers.parse(user_data['answer_phone'], "RU")
    except NumberParseException:
        await message.answer("Номер телефона указан некорректно! Создайте запрос заново!")
        await state.finish()
        await state.reset_state()
        return
    if phonenumbers.is_valid_number(mynumber):
        await message.answer("Напишите Ваш вопрос!")
    else:
        await message.answer("Номер телефона указан некорректно! Создайте запрос заново!")
        await state.finish()
        await state.reset_state()
        return
    # await message.answer(f"Ваше имя: {user_data['answer_name']}")
    # await message.answer(
    #     "Пожалуйста укажите Ваш номер телефона.")
    # await Callback_steps.answ_phone.set()
    await Questions_steps.qwst_text.set()


@dp.message_handler(state=Questions_steps.qwst_text)
async def set_phone(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer_text=answer)

    user_data = await state.get_data()
    get_addr1c.set_questions_1c_brome(user_data['answer_name'], user_data['answer_phone'], user_data['answer_text'])
    await message.answer("Благодарим Вас за обращение в нашу компанию! Мы непременно ответим Вам!")
    await mail.sendmail(f'user: {message.chat.values}; data: {user_data}', state)
    await state.finish()
    await state.reset_state()

