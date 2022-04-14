from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Наш адрес 📨'),
            KeyboardButton(text='Режим работы ⏰')
        ],
        [
            KeyboardButton(text='Задать вопрос 📢'),
            KeyboardButton(text='Обратный звонок 📞')
        ],
        [
            KeyboardButton(text='Узнать цену и наличие товара ₽'),
        ],
[
            KeyboardButton(text='Акции и скидки 📉'),
        ],
[
            KeyboardButton(text='Наши реквизиты 📄'),
        ]
    ]
    , resize_keyboard=True
)