from datetime import datetime

from src.masks_project import get_mask_card_number, get_mask_account

"""В модуле преобразуется формат даты, и маскировка ромеров карт и банковских счетов"""


def get_date(iso_date_str: str) -> str:
    """Преобразует дату из формата ISO8601 в формат 'DD.MM.YYYY'"""

    cleaned_iso_date = iso_date_str.split(".")[0]
    date_obj = datetime.strptime(cleaned_iso_date, "%Y-%m-%dT%H:%M:%SZ")
    return date_obj.strftime("%d.%m.%Y")


def get_date_json(iso_date_str: str) -> str:
    """Преобразует дату из формата ISO8601 в формат 'DD.MM.YYYY'"""

    cleaned_iso_date = iso_date_str.split(".")[0]
    date_obj = datetime.strptime(cleaned_iso_date, "%Y-%m-%dT%H:%M:%S")
    return date_obj.strftime("%d.%m.%Y")


"""Преобразование в формат маска счетов и карт"""


def mask_account_card(account_string: str) -> str:
    account_string = str(account_string)
    account_name = ""
    card_string = list()
    for i in account_string:
        if i.isalpha():
            account_name += i
    for i in account_string:
        if i.isdigit():
            card_string.append(i)
    if account_string.startswith("Счет"):
        return f"Счет {get_mask_account("".join(card_string))}"
    else:
        masked_card = get_mask_card_number("".join(card_string))
        return account_name + " " + masked_card
