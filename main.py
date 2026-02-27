from re import search
import re
from src.search_operations import process_bank_search
# from src.reading_file_csv import reading_csv
from src.reading_file_excel import reading_excel
#from src.utils import get_transaction_data
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
    #return process_bank_search(get_transaction_data, 'EXECUTED')
    result = reading_excel(r"C:\Users\acer\Downloads\transactions_excel.xlsx")
    text = re.search('executed', '')
    result_one = process_bank_search(result,text)
    print(result_one)

if __name__ == "__main__":
    main()
