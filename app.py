from aiogram import executor

from handlers.users.menu import show_menu
from loader import dp
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)

    # Покажем главное меню
    show_menu

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

