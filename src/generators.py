import json


def filter_by_currency(transactions, currency):
    """Функция принимает список словарей и возвращает итератор, который выдает транзакции,
     где валюта операции соответствует заданной"""
    if transactions == []:
        raise ValueError("Введите данные для обработки")
    transaction_usd = (
        transaction for transaction in transactions if transaction["operationAmount"]["currency"]["code"] == currency
    )
    return transaction_usd


if __name__ == "__main__":
    with open("transactions.txt", "r", encoding="utf-8") as file:
        transactions = json.load(file)

    usd_transactions = filter_by_currency(transactions, "USD")
    for _ in range(3):
        print(next(usd_transactions))



def transaction_descriptions(transactions):
    """Генератор transaction_descriptions, принимает список словарей с транзакциями и по очереди возвращает
    описание каждой операции"""
    if transactions == []:
        raise ValueError("Введите данные для обработки")

    for transaction in transactions:
        yield transaction["description"]


if __name__ == "__main__":
    with open("transactions.txt", "r", encoding="utf-8") as file:
        transactions = json.load(file)

    descriptions = transaction_descriptions(transactions)
    for _ in range(3):
        #range(5):
       # print(next(descriptions))
       print(next(descriptions))

import random


def card_number_generator(start: int, stop: int):
    # for _ in range(start, stop):
    #     num = random.randint(start, stop)
    #     num_str = f"{num:016d}"
    #     formatted_number = f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:]}"
    #     yield formatted_number
    """Генератор , выдает номера банковских карт в формате хххх хххх хххх хххх , где х - цифра
номера карты. Генератор должен принимать начальное и конечное значение для генерации диапозона номеров"""
    for num in range(start, stop + 1):
        num_str = f"{num:016d}"
        formatted_number = f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:]}"
        yield formatted_number


if __name__ == "__main__":
    for card_number in card_number_generator(start=1, stop=2):
        print(card_number)
