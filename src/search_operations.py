import random
import re
from collections import defaultdict
from typing import Dict, List

from src.widget_project import get_date, get_date_json, mask_account_card


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """
    Ищет в списке словарей по ключу 'description' строки, содержащие search (регулярное выражение).
    Возвращает список словарей, соответствующих условию.
    """
    pattern = re.compile(search, re.IGNORECASE)  # Игнорируем регистр для поиска
    result = []

    for record in data:
        # print(f"Проверяем операцию: {record}")  # Выводим каждую операцию для проверки
        description = record.get('state', '')

        if isinstance(description, str) and pattern.search(description):
            # print(f"Найдена операция: {record}")  # Выводим операцию, если она подходит
            result.append(record)
    state_list = result

    return state_list


def sort_by_date(state_list: List[Dict], reverse: bool = True) -> List[Dict]:
    """Сортируем список словарей  по ключю key присваивая значение date через
    функцию lambda, убывание организуем через reverse и аннотацию типов bool=True"""
    result_sorted = sorted(state_list, key=lambda item: item["date"], reverse=reverse)

    return result_sorted


def sort_by_date_growth(state_list: List[Dict], reverse: bool = None) -> List[Dict]:
    """Сортируем список словарей  по ключю key присваивая значение date через
    функцию lambda, возростание организуем через reverse=False и аннотацию типов bool=None"""
    result_sorted = sorted(state_list, key=lambda item: item["date"], reverse=False)

    return result_sorted


def process_bank_currency(result_sorted: List[Dict], search: str) -> List[Dict]:
    """
    Ищет в списке словарей по ключу 'description' строки, содержащие search (регулярное выражение).
    Возвращает список словарей, соответствующих условию.
    """
    pattern = re.compile(search, re.IGNORECASE)  # Игнорируем регистр для поиска

    result = []
    for record in result_sorted:
        # Выводим каждую операцию для проверки
        description = record.get('currency_code', '')
        # print(f"Описание: {description}")
        if isinstance(description, str) and pattern.search(description):
            # print(f"Найдена операция: {record}")  # Выводим операцию, если она подходит
            result.append(record)

    state_list_currency = result

    return state_list_currency


def process_bank_currency_json(result_sorted: List[Dict], search: str) -> List[Dict]:
    """
    Ищет в списке словарей по ключу 'description' строки, содержащие search (регулярное выражение).
    Возвращает список словарей, соответствующих условию.
    """
    pattern = re.compile(search, re.IGNORECASE)  # Игнорируем регистр для поиска

    result = []
    for record in result_sorted:
        # Выводим каждую операцию для проверки
        description = record['operationAmount']['currency'].get('code', '')
        # print(f"Описание: {description}")
        if isinstance(description, str) and pattern.search(description):
            # Выводим операцию, если она подходит
            result.append(record)

    state_list_currency = result
    return state_list_currency


def process_bank_operations(result_rub: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по каждой категории на основе поля 'description'.
    Использует регулярные выражения для поиска, а также random для случайных целей
    (например, при отсутствии совпадений).
    """
    # Создаем словарь с дефолтным значением 0 для каждой категории
    category_counts = defaultdict(int)

    # Предварительно формируем регулярные выражения для каждой категории
    category_patterns = {
        cat: re.compile(re.escape(cat), re.IGNORECASE)
        for cat in categories
    }

    for record in result_rub:
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
    result_1 = dict(category_counts)

    return result_1


def print_sorted_category(result_count_categories: Dict[str, int]) -> int:
    """
    Подсчитываем общее количество банковских операций в выборке
    """
    sum_result = sum(result_count_categories.values())
    print(f'\nВсего банковских операций в выборке: {sum_result}')


def print_sorted(text_dict):
    """
    Функция выводит в консоль итоговый результат работы всех функций в выбранном формате
    """
    for text_1 in text_dict:
        from_value = text_1.get('from', 'Не указано')

        # Проверяем, является ли значение строкой
        if isinstance(from_value, str):
            masked_from = mask_account_card(from_value)
        else:
            # print("Значение 'from' не является строкой:", from_value)
            # Обрабатываем случай, если значение не строка
            # Например, игнорируем или преобразуем в строку
            masked_from = "Неизвестно"

        masked_from = mask_account_card(text_1['from'])
        masked_to = mask_account_card(text_1['to'])
        date_format = get_date(text_1['date'])

        final_result = (f'{date_format}  {text_1['description']}\n{masked_from} -> '
                        f'{masked_to}\nСумма:{text_1['amount']} {text_1['currency_code']}\n')

        print(f'{date_format}  {text_1['description']}\n{masked_from} -> '
              f'{masked_to}\nСумма:{text_1['amount']} {text_1['currency_code']}\n')
    return final_result


def print_sorted_json(text_dict):
    """
        Функция выводит в консоль итоговый результат работы всех функций в выбранном формате
        """
    for text_1 in text_dict:
        masked_from = mask_account_card(text_1.get('from', 'Не указано'))
        masked_to = mask_account_card(text_1.get('to', 'Не указано'))
        date_format = get_date_json(text_1['date'])
        if text_1.get('from', 'Не указано') == 'Не указано':
            final_result = (f'{date_format}  {text_1['description']}\n{masked_to}\n'
                            f'Сумма:{text_1['operationAmount']['amount']} '
                            f'{text_1['operationAmount']['currency']['code']}\n')
        else:
            final_result = (f'{date_format}  {text_1['description']}\n{masked_from} -> '
                            f'{masked_to}\nСумма:{text_1['operationAmount']['amount']} '
                            f'{text_1['operationAmount']['currency']['code']}\n')
        print(final_result)

    return final_result
