import pandas as pd


address_file_csv = r'https://github.com/skypro-008/transactions/raw/main/transactions.csv?plain=1'

"""Функция принимает на вход путь до файла CSV и выдаёт список словарей с транзакциями"""

def reading_csv(address_csv: str) -> list:

    pd_file = pd.read_csv(address_csv, delimiter=';')
    result = pd_file.to_dict(orient='records')

    return result


if __name__ == "__main__":
    print(reading_csv(address_file_csv))