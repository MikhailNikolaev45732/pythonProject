import pandas as pd
import json
# from idlelib.iomenu import encoding


address_file_excel = r"C:\Users\acer\Downloads\transactions_excel.xlsx"

"""Функция принимает на вход путь до файла EXCEL и выдаёт список словарей с транзакциями"""


def reading_excel(address_ex: str) -> list:
    pd_file = pd.read_excel(address_ex)
    result = pd_file.fillna('').to_dict(orient='records')
    with open('../data/transactions_excel.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False, indent=4)

    return result


if __name__ == "__main__":
    print(reading_excel(address_file_excel))
