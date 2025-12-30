import pytest
from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from src.generators import card_number_generator
import json
#from conftest import filter_by_currency_e
#with open('src.transactions.txt', 'r', encoding='utf-8') as file:
   # transactions = json.load(file)


# В этом блоке собраны фикстуры для каждой из функцый которые вызываются в ниже написанных тестах
@pytest.fixture
def filter_by_currency_e():
    """Фикстура список словарей (банковские операции) отфильтрованные по валюте операций"""
    return [{
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        }]


@pytest.fixture
def transactions():
    """Фикстура список словарей (банковские операции)"""
    return [{
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
            }]


@pytest.fixture
def description():
    """Фикстура список операций"""
    return ["Перевод организации",
           "Перевод со счета на счет",
           "Перевод со счета на счет",
           "Перевод с карты на карту",
           "Перевод организации"]


# Тесты для функций модуля generators.py с помощю фикстур, тесты возвращают ожидаемый результат.
def test_filter_by_currency(transactions, filter_by_currency_e):
     result = list(filter_by_currency(transactions, 'USD'))
     assert result == filter_by_currency_e


def test_filter_by_currency_invalid():
    with pytest.raises(ValueError):
        filter_by_currency([], [])


def test_transaction_descriptions(transactions, description):
    result = list(transaction_descriptions(transactions))
    assert result == description


# def test_transaction_descriptions_invalid():
#     with pytest.raises(ValueError):
#         transaction_descriptions([])


# Генератор номеров банковских карт, тестируем при помощи параметризации данных, возвращается
# ожидаемый результат
@pytest.mark.parametrize("start, stop, expected_cards", [
    (4000000000000000, 4000000000000002, ["4000 0000 0000 0000", "4000 0000 0000 0001", "4000 0000 0000 0002"]),
    (4000000000000005, 4000000000000007, ["4000 0000 0000 0005", "4000 0000 0000 0006", "4000 0000 0000 0007"]),
])
def test_card_number_generator(start, stop, expected_cards):
    result = list(card_number_generator(start, stop))
    assert result == expected_cards
