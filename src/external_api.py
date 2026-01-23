import os
import requests
from dotenv import load_dotenv
import json


load_dotenv()
API_KEY = os.getenv("API_KEY")


def currency_conversion(transaction: dict) -> float:
    """Функция осуществляет конвертацию суммы транзакции в рубли"""
    try:
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]

        if currency != "RUB":
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
            payload = {}
            headers = {"apikey": API_KEY}
            response = requests.request("GET", url=url, headers=headers, data=payload)
            status_code = response.status_code
            result = json.loads(response.text)
            amount_rub = float(result['result'])
            return amount_rub
            if status_code != 200:
                print(f"Ошибка запроса: Код {status_code}, Описание: {result}")
                return 0.0

            else:
                return f"Запрос не выполнен.\nКод ошибки: {status_code}.\nОписание ошибки: {result}."
        else:
            return amount
    except Exception as e:
        print(f"Ошибка конвертации: {e}")
        return 0.0


if __name__ == "__main__":
    print(
        currency_conversion(
            {
                "id": 649467725,
                "state": "EXECUTED",
                "date": "2018-04-14T19:35:28.978265",
                "operationAmount": {"amount": "9995.73", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Счет 27248529432547658655",
                "to": "Счет 97584898735659638967",
            },
        )
    )

    print(
        currency_conversion(
            {
                "id": 782295999,
                "state": "EXECUTED",
                "date": "2019-09-11T17:30:34.445824",
                "operationAmount": {"amount": "4280.01", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 24763316288121894080",
                "to": "Счет 96291777776753236930",
            }
        )
    )
