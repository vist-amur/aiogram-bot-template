from brom import *
from data import config


def get_addr1c_brome():
    login = config.LOGIN1C
    client = БромКлиент(config.PUB1C, login.encode("utf-8"), config.PASS1C)
    info = client.Рф_Телеграм.АдресОрганизации()

    return info


def get_clock_1c_brome():
    login = config.LOGIN1C
    client = БромКлиент(config.PUB1C, login.encode("utf-8"), config.PASS1C)
    info = client.Рф_Телеграм.РежимРаботы()

    return info


def set_callback_1c_brome(nname, nphone):
    login = config.LOGIN1C
    client = БромКлиент(config.PUB1C, login.encode("utf-8"), config.PASS1C)
    info = client.Рф_Телеграм.ЗаписатьОбращениеИзТелеграм(nname, "Запрос обратного звонка", nphone)

    return info


def set_questions_1c_brome(nname, nphone, ntext):
    login = config.LOGIN1C
    client = БромКлиент(config.PUB1C, login.encode("utf-8"), config.PASS1C)
    info = client.Рф_Телеграм.ЗаписатьОбращениеИзТелеграм(nname, ntext, nphone)

    return info


def get_price_1c_brome(keywords):
    login = config.LOGIN1C
    client = БромКлиент(config.PUB1C, login.encode("utf-8"), config.PASS1C)
    info = client.Рф_Телеграм.ПолучитьОстаткиИЦены(keywords)
    pK = ""
    pPr = ""
    pOst = ""
    list_dict = []
    if not info:
        return []
    for i, y in enumerate(info):
        if str(y.Номенклатура).lower().find('brom.') != -1:
            continue

        if str(y.Коэффициент).lower().find('brom.') != -1:
            pK = '0'
        else:
            pK = y.Коэффициент

        if str(y.Остаток).lower().find('brom.') != -1:
            pOst = '0'
        else:
            pOst = y.Остаток

        if str(y.Цена).lower().find('brom.') != -1:
            pPr = '0'
        else:
            pPr = y.Цена

        dict_answer = {"Номенклатура": y.Номенклатура.Наименование, "Артикул": y.Номенклатура.Артикул,
                       "Коэффициент": pK, "Остаток": pOst,
                       "Цена": pPr}
        list_dict.append(dict_answer)
    return list_dict


def get_null():
    return "Повторите запрос"


def get_requisites_1c_brome():
    login = config.LOGIN1C
    client = БромКлиент(config.PUB1C, login.encode("utf-8"), config.PASS1C)
    info = client.Рф_Телеграм.НашиРеквизиты()

    return info


def get_discounts_1c_brome():
    login = config.LOGIN1C
    client = БромКлиент(config.PUB1C, login.encode("utf-8"), config.PASS1C)
    info = client.Рф_Телеграм.ПолучитьАкции()

    list_dict = []
    if info == 'Сервер не доступен!':
        return []
    for i, y in enumerate(info):
        dict_answer = {"Номенклатура": y.Номенклатура.Наименование, "Артикул": y.Номенклатура.Артикул,
                       "Старая цена": y.Сумма, "Новая цена": y.НоваяЦена, "Дата окончания акции": y.ДатаОкончания}
        list_dict.append(dict_answer)

    return list_dict
