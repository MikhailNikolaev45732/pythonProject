import sys
from src.search_operations import process_bank_search
from src.search_operations import sort_by_date
from src.search_operations import sort_by_date_growth
from src.search_operations import process_bank_currency
from src.search_operations import process_bank_operations
from src.search_operations import print_sorted
from src.search_operations import print_sorted_json
from src.search_operations import process_bank_currency_json
from src.search_operations import print_sorted_category
from src.reading_file_csv import reading_csv
from src.reading_file_excel import reading_excel
from src.utils import get_transaction_data
from pathlib import Path


def main():
    """Главная функция для работы с приложениями проекта"""
    print(
        '''Привет! Добро пожаловать в программу работы
        с банковскими транзакциями.
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла'''
    )

    BASE_DIR = Path(__file__).resolve().parent

    result_csv_ = BASE_DIR / "data" / "transactions.csv"
    result_json_ = BASE_DIR / "data" / "operations.json"
    result_exe_ = BASE_DIR / "data" / "transactions_excel.xlsx"

    result_exe = reading_excel(result_exe_)
    result_csv = reading_csv(result_csv_)
    result_json = get_transaction_data(result_json_)

    user_choic_f = int(input('Введите номер операции: '))
    print(
        '''Введите статус, по которому необходимо выполнять фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING'''
    )

    valid_statuses = ["executed", "canceled", "pending"]
    search = ""

    while search not in valid_statuses:
        search = input('Введите статус: \n').lower()
        if search not in valid_statuses:
            print(f'Статус операции "{search}" недоступен.')
            print('Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')

    if user_choic_f == 1:
        data = result_json

    elif user_choic_f == 2:
        data = result_csv

    elif user_choic_f == 3:
        data = result_exe

    result = process_bank_search(data, search)
    state_list = result
    state_list = process_bank_search(data, search)

    if not state_list:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.')
        sys.exit()

    print(
        """Отсортировать операции по дате?"""
    )
    valid_statuses_1 = ["да", "нет"]
    user_data = ""

    while user_data not in valid_statuses_1:
        user_data = input('да/нет: \n').lower()
        if user_data not in valid_statuses_1:
            print(f'Вариант "{user_data}" недоступен.')
            print('Доступные варианты: да/нет')

    if user_data == 'да':
        print(
            """Отсортировать по возрастанию или убыванию?"""
        )
        valid_statuses_2 = ['по возрастанию', 'по убыванию']
        user_data_direction = ""

        while user_data_direction not in valid_statuses_2:
            user_data_direction = input('по возрастанию/по убыванию: \n').lower()
            if user_data_direction not in valid_statuses_2:
                print(f'Вариант "{user_data_direction}" недоступен.')
                print('Доступные варианты: по возрастанию/по убыванию')

        if user_data_direction == 'по убыванию':
            result_sorted_ = sort_by_date(state_list)
        elif user_data_direction == 'по возрастанию':
            result_sorted_ = sort_by_date_growth(state_list)
            result_sorted = result_sorted_
    elif user_data == 'нет':
        pass

    print(
        """Выводить только рублёвые транзакции?"""
    )
    valid_statuses_3 = ["да", "нет"]
    user_data_currency = ""

    while user_data_currency not in valid_statuses_3:
        user_data_currency = input('да/нет: \n').lower()
        if user_data_currency not in valid_statuses_3:
            print(f'Вариант "{user_data_currency}" недоступен.')
            print('Доступные варианты: да/нет')

    if user_data == 'да':
        if user_choic_f == 2 or user_choic_f == 3:
            if user_data_currency == 'да':
                search = 'RUB'
                result_currency_rub = process_bank_currency(result_sorted_, search)
            elif user_data_currency == 'нет':
                result_currency_rub = result_sorted_
            state_list_currency = result_currency_rub
            result_rub = state_list_currency
        elif user_choic_f == 1:
            if user_data_currency == 'да':
                search = 'RUB'
                result_currency_rub = process_bank_currency_json(result_sorted_, search)
            elif user_data_currency == 'нет':
                result_currency_rub = result_sorted_
            state_list_currency = result_currency_rub
            result_rub = state_list_currency
    elif user_data == 'нет':
        if user_choic_f == 2 or user_choic_f == 3:
            if user_data_currency == 'да':
                search = 'RUB'
                result_currency_rub = process_bank_currency(state_list, search)
            elif user_data_currency == 'нет':
                result_currency_rub = state_list
            state_list_currency = result_currency_rub
            result_rub = state_list_currency
        elif user_choic_f == 1:
            if user_data_currency == 'да':
                search = 'RUB'
                result_currency_rub = process_bank_currency_json(state_list, search)
            elif user_data_currency == 'нет':
                result_currency_rub = state_list
            state_list_currency = result_currency_rub
            result_rub = state_list_currency

    if not state_list_currency:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.')
        sys.exit()

    print(
        """Отфильтровать список транзакций по определённому слову в описании?"""
    )
    valid_statuses_4 = ["да", "нет"]
    user_data_description = ""

    while user_data_description not in valid_statuses_4:
        user_data_description = input('да/нет: \n').lower()
        if user_data_description not in valid_statuses_4:
            print(f'Вариант "{user_data_description}" недоступен.')
            print('Доступные варианты: да/нет')

    if user_data_description == 'да':
        categories = ['Перевод со счета на счет', 'Перевод с карты на карту', 'Открытие вклада', 'Перевод организации']
        result_count_categories = process_bank_operations(result_rub, categories)
        sorted_category = print_sorted_category(result_count_categories)
    print(
        """Распечатываю итоговый список транзакций ...\n"""
    )

    text_dict = result_rub
    if user_choic_f == 1:
        result_final_sorted = print_sorted_json(text_dict)
    else:
        result_final_sorted = print_sorted(text_dict)

        return result_final_sorted


if __name__ == "__main__":
    main()
