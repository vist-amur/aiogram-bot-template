from aiogram.dispatcher.filters.state import StatesGroup, State


class Questions_steps(StatesGroup):
    qwst_name = State()
    qwst_phone = State()
    qwst_text = State()
