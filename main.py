from re import search
import re
from src.search_operations import process_bank_search
from src.search_operations import sort_by_date
from src.search_operations import sort_by_date_growth
from src.search_operations import process_bank_currency
from src.search_operations import process_bank_operations
from src.reading_file_csv import reading_csv
from src.reading_file_excel import reading_excel
from src.utils import get_transaction_data
import json
import os
import logging
#from src import utils

def main():
    #1
    # print("Текущая рабочая директория:", os.getcwd())
    """Главная функция для работы с приложениями проекта"""
    print(
        '''Привет! Добро пожаловать в программу работы
        с банковскими транзакциями.
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла'''
    )
    result_exe = reading_excel(r"C:\Users\acer\Downloads\transactions_excel.xlsx")
    result_csv = reading_csv(r'https://github.com/skypro-008/transactions/raw/main/transactions.csv?plain=1')
    result_json = get_transaction_data(r'C:\Users\acer\exampl\pythonProject/data/operations.json')
    #print(result_json)
    user_choic_f = int(input('Введите номер операции: '))
    print(
        '''Введите статус, по которому необходимо выполнять фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING'''
    )

    search = str(input('Введите статус: '))
    if user_choic_f == 1:
        data = result_json
        #return process_bank_search(data, search)
    elif user_choic_f == 2:
        data = result_csv
        #return process_bank_search(data, search)
    elif user_choic_f == 3:
        data = result_exe
        #return process_bank_search(data, search)

    result = process_bank_search(data, search)
    state_list = result

    print(
        """Отсортировать операции по дате?"""
    )
    user_data = str(input('да/нет :'))
    print(
        """Отсортировать по возрастанию или убыванию?"""
    )
    user_data_direction = str(input('по возрастанию/по убыванию :'))

    if user_data_direction == 'по убыванию':
        result_sorted_ = sort_by_date(state_list)
    elif user_data_direction == 'по возрастанию':
        result_sorted_ = sort_by_date_growth(state_list)
    result_sorted = result_sorted_
    print(
        """Выводить только рублёвые транзакции?"""
    )
    user_data_currency = str(input('да/нет :'))

    if user_data_currency == 'да':
        search = 'RUB'
        result_currency_rub = process_bank_currency(result_sorted, search)
    elif user_data_currency == 'нет':
        result_currency_rub = result_sorted
    print(
        """Отфильтровать список транзакций по определённому слову в описании?"""
    )
    user_data_description = str(input('да/нет :'))

    if user_data_description == 'да':
        categories = ['Перевод со счета на счет', 'Перевод с карты на карту', 'Открытие вклада', 'Перевод организации']
        result_count_categories = process_bank_operations(result_currency_rub, categories)
    print(
        """Распечатываю итоговый список транзакций ..."""
    )

    # if user_data_direction == 'по убыванию':
    #     return sort_by_date(state_list)


if __name__ == "__main__":

    main()
