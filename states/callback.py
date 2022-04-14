from aiogram.dispatcher.filters.state import StatesGroup, State


class Callback_steps(StatesGroup):
    answ_name = State()
    answ_phone = State()
    answ_email = State()