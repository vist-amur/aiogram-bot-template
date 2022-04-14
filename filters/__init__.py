from aiogram import Dispatcher

from loader import dp
from .addr import isAddr


if __name__ == "filters":
    dp.filters_factory.bind(isAddr)

