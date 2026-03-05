import random
import re
from collections import defaultdict
from typing import Dict, List

"""Напишите функцию, которая будет принимать список словарей с данными о банковских операциях
 и строку поиска, а возвращать список словарей, у которых в описании есть данная строка. 
 При реализации этой функции используйте библиотеку re"""

def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """
    Ищет в списке словарей по ключу 'description' строки, содержащие search (регулярное выражение).
    Возвращает список словарей, соответствующих условию.
    """
    pattern = re.compile(search, re.IGNORECASE)  # Игнорируем регистр для поиска

    result = []
    for record in data:
        #print(f"Проверяем операцию: {record}")  # Выводим каждую операцию для проверки
        description = record.get('state', '')
        #print(f"Описание: {description}")
        if isinstance(description, str) and pattern.search(description):
            #print(f"Найдена операция: {record}")  # Выводим операцию, если она подходит
            result.append(record)

    state_list = result
    print('Результат поиска:', state_list)
    return state_list


def sort_by_date(state_list: List[Dict], reverse: bool = True) -> List[Dict]:
    """Сортируем список словарей  по ключю key присваивая значение date через
    функцию lambda, убывание организуем через reverse и аннотацию типов bool=True"""
    result_sorted = sorted(state_list, key=lambda item: item["date"], reverse=reverse)
    print('Результат сортировки даты по убыванию:', result_sorted)
    return result_sorted


def sort_by_date_growth(state_list: List[Dict], reverse: bool = None) -> List[Dict]:
    """Сортируем список словарей  по ключю key присваивая значение date через
    функцию lambda, возростание организуем через reverse=False и аннотацию типов bool=None"""
    result_sorted = sorted(state_list, key=lambda item: item["date"], reverse=False)
    print('Результат сортировки даты по возрастанию:', result_sorted)
    return result_sorted


def process_bank_currency(result_sorted: List[Dict], search: str) -> List[Dict]:
    """
    Ищет в списке словарей по ключу 'description' строки, содержащие search (регулярное выражение).
    Возвращает список словарей, соответствующих условию.
    """
    pattern = re.compile(search, re.IGNORECASE)  # Игнорируем регистр для поиска

    result = []
    for record in result_sorted:
        #print(f"Проверяем операцию: {record}")  # Выводим каждую операцию для проверки
        description = record.get('currency_code', '')
        #print(f"Описание: {description}")
        if isinstance(description, str) and pattern.search(description):
            #print(f"Найдена операция: {record}")  # Выводим операцию, если она подходит
            result.append(record)

    state_list_currency = result
    print('Результат поиска по названию валюты:', state_list_currency)
    return state_list_currency


def process_bank_operations(result_currency_rub: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по каждой категории на основе поля 'description'.
    Использует регулярные выражения для поиска, а также random для случайных целей (например, при отсутствии совпадений).
    """
    # Создаем словарь с дефолтным значением 0 для каждой категории
    category_counts = defaultdict(int)

    # Предварительно формируем регулярные выражения для каждой категории
    category_patterns = {
        cat: re.compile(re.escape(cat), re.IGNORECASE)
        for cat in categories
    }

    for record in result_currency_rub:
        description = record.get('description', '')
        matched_category = None

        # Проверяем описание на совпадение с категориями
        for cat, pattern in category_patterns.items():
            if pattern.search(description):
                category_counts[cat] += 1
                matched_category = cat
                break  # нашли категорию, идем к следующей операции

        # Если ни одна категория не совпала, можно присвоить "прочие" или случайную категорию
        if matched_category is None:
            # Вариант с рандомным выбором категории
            random_cat = random.choice(categories)
            category_counts[random_cat] += 1

    # Преобразуем defaultdict в обычный dict перед возвратом
    result = dict(category_counts)
    print('непонятная функция', result)

    return result

