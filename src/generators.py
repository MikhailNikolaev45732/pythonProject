import json


# Функция возвращает итератор, который выдает транзакции, где валюта операции соответствует заданной
def filter_by_currency(transactions, currency):
    """Задаем перебор словарей по ключу currency"""
    if transactions == []:
        raise ValueError("Введите данные для обработки")
    transaction_usd = (
        transaction for transaction in transactions if transaction["operationAmount"]["currency"]["code"] == currency
    )
    return transaction_usd


if __name__ == "__main__":
    """Обращаемся к списоку словарей в файле transactions.txt"""
    with open("transactions.txt", "r", encoding="utf-8") as file:
        transactions = json.load(file)

    usd_transactions = filter_by_currency(transactions, "USD")
    for _ in range(3):
        print(next(usd_transactions))


# Генератор transaction_descriptions, принимает список словарей с транзакциями и возвращает описание каждой
# операции по очереди
def transaction_descriptions(transactions):
    if transactions == []:
        raise ValueError("Введите данные для обработки")
    description_list = (transaction["description"] for transaction in transactions)
    return description_list


if __name__ == "__main__":
    """Обращаемся к списоку словарей в файле transactions.txt"""
    with open("transactions.txt", "r", encoding="utf-8") as file:
        transactions = json.load(file)

    descriptions = transaction_descriptions(transactions)
    for _ in range(5):
        print(next(descriptions))


# import random
def card_number_generator(start: int, stop: int):
    # for _ in range(start, stop):
    #     num = random.randint(start, stop)
    #     num_str = f"{num:016d}"
    #     formatted_number = f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:]}"
    #     yield formatted_number

    for num in range(start, stop + 1):
        num_str = f"{num:016d}"
        formatted_number = f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:]}"
        yield formatted_number


if __name__ == "__main__":
    for card_number in card_number_generator(start=1, stop=2):
        print(card_number)
