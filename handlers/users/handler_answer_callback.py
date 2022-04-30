import phonenumbers
from aiogram import types
from aiogram.dispatcher import FSMContext
from phonenumbers import NumberParseException

from loader import dp

from states import Callback_steps
from handlers.users.menu import get_sales
from utils.misc import get_addr1c
from utils.misc import mail



@dp.message_handler(text='Обратный звонок 📞')
async def answ_name(message: types.Message):
    await message.answer(
        "Для совершения обратного звонка, пожалуйста, уточните информацию! Как к Вам можно обращаться?")
    await Callback_steps.answ_name.set()


@dp.message_handler(state=Callback_steps.answ_name)
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
    if answer == 'Задать вопрос 📢':
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
        #return await message.answer(get_addr1c.get_discounts_1c_brome())
        return await get_sales(message)
    if answer == 'Наши реквизиты 📄':
        await state.finish()
        await state.reset_state()
        return await message.answer(get_addr1c.get_requisites_1c_brome())

    await state.update_data(answer_name=answer)

    await message.answer(
        "Пожалуйста укажите Ваш номер телефона.")
    await Callback_steps.answ_phone.set()


@dp.message_handler(state=Callback_steps.answ_phone)
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
        get_addr1c.set_callback_1c_brome(user_data['answer_name'], user_data['answer_phone'])
        await message.answer("Благодарим Вас за обращение в нашу компанию! Мы непременно перезвоним Вам!")
        await mail.sendmail(f'user {str(message.chat.values["id"])} firstname {message.chat.values["username"]}', state)
    else:
        await message.answer("Номер телефона указан некорректно! Создайте запрос заново!")
        await state.finish()
        await state.reset_state()
    # await message.answer(f"Ваше имя: {user_data['answer_name']}")
    # await message.answer(
    #     "Пожалуйста укажите Ваш номер телефона.")
    # await Callback_steps.answ_phone.set()
    await state.finish()
    await state.reset_state()
