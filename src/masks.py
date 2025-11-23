"""Функция get_mask_card_number принимает на вход номер карты и возвращает
   её маску
   входной аргумент: 7000792289606361
   выход функции: 7000 79** ****6361"""


def get_mask_card_number(card_number: int) -> str:
    """Функция  принимает на вход номер карты и возвращает ее маску."""
    card_str = str(card_number)
    return card_str[:4] + " " + card_str[4:6] + "** **** " + card_str[-4:]


"""Функция get_mask_account принимает на вход номер счета и возвращает
   его маску
   входной аргумент: 73654108430135874305
   выход функции: **4305"""


def get_mask_account(account_number: int) -> str:
    """Функция  принимает на вход номер счета и возвращает его маску."""
    account_str = str(account_number)
    return "**" + account_str[-4:]
