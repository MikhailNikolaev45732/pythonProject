import json
import os
import logging


# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     filename='../logs/utils.log',
#     encoding='utf-8',
#     filemode='w'
# )


#transaction_logger = logging.getLogger('transaction.data')

"""Функция принимает на вход путь до JSON-файла и возвращает   список словарей с данными о финансовых транзакциях."""


def get_transaction_data(filepath: str) -> list[dict]:
    #transaction_logger.info("Функция принимает путь до JSON-файла")
    try:
        with open(filepath, "r", encoding="utf-8") as transaction_file:
            try:
                transaction_data = json.load(transaction_file)
                #transaction_logger.info("Функция успешно нашла и декодировала JSON-файл")
                #print(transaction_data)
                #result = transaction_data.to_dict(orient='records')
                #print(result)
                return transaction_data
            except json.JSONDecodeError:
                #transaction_logger.error("Функция не смогла декодировать файл, проверь методы")
                print("Ошибка декодирования файла")
                return []
    except FileNotFoundError:
        #transaction_logger.info(f"Файл {filepath} не найден")
        print(f"Файл {filepath} не найден")
        return []


if __name__ == "__main__":
    print(get_transaction_data(os.path.join(os.path.dirname(__file__), '../src/operations.json')))
