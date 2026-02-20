import pandas as pd


address_file_excel = r"C:\Users\acer\Downloads\transactions_excel.xlsx"

"""Функция принимает на вход путь до файла EXCEL и выдаёт список словарей с транзакциями"""

def reading_excel(address_ex: str) -> list:
    pd_file = pd.read_excel(address_ex)
    result = pd_file.to_dict(orient='records')

    return result


if __name__ == "__main__":
    print(reading_excel(address_file_excel))


