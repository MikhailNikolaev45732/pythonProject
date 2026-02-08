"""Функция get_mask_card_number принимает на вход номер карты и возвращает
её маску
входной аргумент: 7000792289606361
выход функции: 7000 79** ****6361"""


def get_mask_card_number(card_number: int) -> str:
    """Функция  принимает на вход номер карты и возвращает ее маску."""
    card_str = str(card_number)
    card_num_len = len(card_str)

    if card_num_len > 0 and card_num_len != 16:
        raise ValueError("Некорректный ввод номера")
    elif card_num_len == 0:
        raise ValueError("Введите номер")

    return card_str[:4] + " " + card_str[4:6] + "** ****" + card_str[-4:]


"""Функция get_mask_account принимает на вход номер счета и возвращает
   его маску
   входной аргумент: 73654108430135874305
   выход функции: **4305"""


def get_mask_account(account_number: int) -> str:
    """Функция  принимает на вход номер счета и возвращает его маску."""
    account_str = str(account_number)
    account_num_len = len(account_str)

    if account_num_len > 0 and account_num_len != 20:
        raise ValueError("Некорректный ввод номера")
    elif account_num_len == 0:
        raise ValueError("Введите номер")

    return "**" + account_str[-4:]

