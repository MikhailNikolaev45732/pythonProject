from datetime import datetime
from masks import get_mask_card_number
from masks import get_mask_account



# def mask_account_card(account_string):
#
#
#     if account_string.startswith("Счет"):
#         """Обработка ввода банковского счета"""
#         _, account_number = account_string.split(maxsplit=1)
#         return f"Счет {'*'*(len(account_number)-4)}{account_number[-4:]}"
#     else:
#         """Обработка карт"""
#         card_type, card_number = account_string.rsplit(maxsplit=1)
#         masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
#         return f"{card_type} {masked_number}"
#
#
#
# def get_date(iso_date_str):
#     """Преобразует дату из формата ISO8601 в формат 'DD.MM.YYYY'"""
#     # Отбрасываем лишнюю информацию после секунды (.671407)
#     cleaned_iso_date = iso_date_str.split('.')[0]
#     # Парсим строку в объект datetime
#     date_obj = datetime.strptime(cleaned_iso_date, "%Y-%m-%dT%H:%M:%S")
#     # Возвращаем строку с датой в нужном формате
#     return date_obj.strftime("%d.%m.%Y")


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


