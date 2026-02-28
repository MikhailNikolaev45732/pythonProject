from re import search
import re
from src.search_operations import process_bank_search
from src.reading_file_csv import reading_csv
from src.reading_file_excel import reading_excel
from src.utils import get_transaction_data
import json
import os
import logging
#from src import utils

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
    result_exe = reading_excel(r"C:\Users\acer\Downloads\transactions_excel.xlsx")
    result_csv = reading_csv(r'https://github.com/skypro-008/transactions/raw/main/transactions.csv?plain=1')
    result_json = get_transaction_data(os.path.join(r'C:/Users/acer/exampl/pythonProject/src/operations.json'))

    user_choic_f = int(input('Введите номер операции: '))
    print(
        '''Введите статус, по которому необходимо выполнять фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING'''
    )

    search = str(input('Введите статус: '))
    if user_choic_f == 1:
        data = result_json
        return process_bank_search(data, search)
    elif user_choic_f == 2:
        data = result_csv
        return process_bank_search(data, search)
    elif user_choic_f == 3:
        data = result_exe
        return process_bank_search(data, search)
    #return process_bank_search(data, 'EXECUTED')
    #result = reading_excel(r"C:\Users\acer\Downloads\transactions_excel.xlsx")
    #text = re.search('executed', '')
    #result_one = process_bank_search(result,text)
    #print(result_one)
        #print(data)
    result = process_bank_search(data, search)
    #print("Результат поиска:", result)
    #print(result_csv)
if __name__ == "__main__":
    main()
