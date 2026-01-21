import os
import requests
from dotenv import load_dotenv
import json


# def converter_currency(transaction: float, currency: str) -> float:
#     """Конвертер валюты в рубли через API"""
#
#     load_dotenv("..src/env")  # запускаем файл .env
#     API_KEY = os.getenv("API_KEY")
#     #API_KEY = f4CxjkSnkwRNb4kX7D6dzgcWVESTDap0# В файле .env забираем апи_ключ
#     # блок отвечающий за ошибки до вызова функции
#     if not isinstance(transaction, (int, float)):
#         print(f"Введена неверная сумма транзакции")
#         return False
#
#
#     #условие валюты
#     currency_to_convert = ["USD", "EUR"]
#     if currency in currency_to_convert:
#
#         # запускаем готовый апи запрос
#         url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={transaction}"
#
#         payload = {}
#         headers = {"apikey": API_KEY}
#
#         response = requests.request("GET", url, headers=headers, data=payload)
#
#         # проверка на ошибки запроса
#         if response.status_code != 200:
#             print(f"Ошибка запроса : {response.status_code}")
#             return False
#         amount: float = round(response.json()["result"], 2)
#         return amount
#     else:
#         print("такой валюты нет в списке")
#     print(API_KEY)
# def get_exchange_rates(amount: float, currency: str) -> float:
#     """ Функция обращения к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли с использованием запроса к         https://apilayer.com/exchangerates_data-api
#     """
#     convert_to = "RUB"
#     request_str = f"https://api.apilayer.com/exchangerates_data/convert?to={convert_to}&from={currency}&amount={amount}"
#     request_header = {"apikey": API_KEY}
#     response = requests.get(request_str, headers=request_header)
#     status_code = response.status_code
#     print(f"Статус код: {status_code}")
#     # Проверяем, что запрос был успешным (статус-код = 200)
#     if status_code == 200:
#         # Проверка возвращаемого результата
#         response_data = response.json()
#         print(response_data)
#         tx_result = responce_data["result"]
#         return round(float(tx_result), 2)
#     else:
#         # Вывод сообщения об ошибке
#         print(f"Запрос не был успешным. Возможная причина: {response.reason}")

def currency_conversion(amount: str, currency: str) -> float:
    """
    Функция для конвертации валюты.
    - param amount: принимает сумму транзакции в виде строки;
    - param currency: принимает тип валюты транзакции в виде строки;
    - return: возвращает сумму транзакции в рублях.
    """

    try:
        load_dotenv(".env")
        api_key = os.getenv('API_KEY')
        #print(api_key)
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        payload = {}
        headers = {"apikey": f"{api_key}"}
        #print(headers)
        response = requests.request("GET", url=url, headers=headers, data=payload)
        print(response.text)
        # status_code = response.status_code
        # result_ = response.text # Если превышено количество запросов, то сообщение: {"message":"You have exceeded your daily\/monthly API rate limit.
        # Please review and upgrade your subscription plan at https:\/\/promptapi.com\/subscriptions to continue."}

        result = json.loads(response.text) #текстовое содержимое ответа преобразуем из строки JSON в объект Python
        #print(result)
        amount_rub = float(result['result'])
        #print(type(amount_rub))

        return amount_rub

    except requests.exceptions.RequestException as e:
        print(f"HTTP ошибка: {e.response.status_code} - {e.response.reason}")
        print(f"Сообщение об ошибке: {e}")

    except json.JSONDecodeError as e:
        print("Ошибка декодирования. Invalid result.")
        print(f"Сообщение об ошибке: {e.msg}")
        print(f"Строка: {e.lineno}, колонка: {e.colno}")

    except TypeError:
        print("The object type is not serializable in JSON format.")

    except Exception as e:
        print(f"Ошибка {e}")
        print(result)


if __name__ == "__main__":
    currency_conversion(1000, "USD")
    #print(api_key)

# load_dotenv(".env")
# api_key = os.getenv("API_KEY")
# print(api_key)
