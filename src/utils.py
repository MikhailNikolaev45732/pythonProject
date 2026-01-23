import json
import os

def get_transaction_data(filepath: str)  -> list[dict]:
    """ Функция принимает на вход путь до JSON-файла и возвращает   список словарей с данными о финансовых транзакциях.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as transaction_file:
            try:
                transaction_data = json.load(transaction_file)
                return transaction_data
            except json.JSONDecodeError:
                print("Ошибка декодирования файла")
                return []
    except FileNotFoundError:
        print(f"Файл {filepath} не найден")
        return []


if __name__ == "__main__":
     print(get_transaction_data(os.path.join(os.path.dirname(__file__), '../data/operations.json')))
