from datetime import datetime
from masks import get_mask_card_number
from masks import get_mask_account


"""В модуле преобразуется формат даты, и маскировка ромеров карт и банковских счетов"""


def get_date(iso_date_str: str) -> str:
    """Преобразует дату из формата ISO8601 в формат 'DD.MM.YYYY'"""
    """Убираем формат секунды"""
    cleaned_iso_date = iso_date_str.split('.')[0]
    """Подставляем в метод преобразованную строку"""
    date_obj = datetime.strptime(cleaned_iso_date, "%Y-%m-%dT%H:%M:%S")
    """Возвращаем строку нужного формата"""
    return date_obj.strftime("%d.%m.%Y")

"""Преобразование в формат маска счетов и карт"""
def mask_account_card(account_string: str) -> str:
    account_name = list()
    for i in account_string:
        if i.isalpha():
            account_name.append("i")
    if account_name == "Счет":
        return f'Счет + " " + {get_mask_account(accound_stribg)}'
    card_string = list()
    if accound_name != "Счет":
        for i in accound_string:
            if i.isdigit():
                card_string.append("i")
        return account_name + " " + get_mask_card_number(card_srting)


