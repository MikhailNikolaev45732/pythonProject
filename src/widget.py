from datetime import datetime
from masks import get_mask_card_number
from masks import get_mask_account


"""В модуле преобразуется формат даты, и маскировка ромеров карт и банковских счетов"""


def get_date(iso_date_str: str) -> str:
    """Преобразует дату из формата ISO8601 в формат 'DD.MM.YYYY'"""
    cleaned_iso_date = iso_date_str.split(".")[0]
    date_obj = datetime.strptime(cleaned_iso_date, "%Y-%m-%dT%H:%M:%S")
    return date_obj.strftime("%d.%m.%Y")


# print(get_date("2024-03-11T02:26:18.671407"))  # Ожидаемый результат: "11.03.2024"


"""Преобразование в формат маска счетов и карт"""


def mask_account_card(account_string: str) -> str:
    account_name = ""
    card_string = list()
    for i in account_string:
        if i.isalpha():
            account_name += i
    if account_string.startswith("Счет"):
        return f"Счет {get_mask_account(account_string)}"
    else:
        for i in account_string:
            if i.isdigit():
                card_string.append(i)
    masked_card = get_mask_card_number("".join(card_string))
    return account_name + " " + masked_card


# print(mask_account_card("Visa Platinum 7000792289606361"))# Ожидаемый результат: "Visa Platinum 7000 79** **** 6361"
# print(mask_account_card("Счет 73654108430135874305"))  # Ожидаемый результат: "Счет **4305"
