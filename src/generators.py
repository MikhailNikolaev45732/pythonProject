import json


def filter_by_currency(transactions, currency):
     transaction_usd = (transaction for transaction in transactions
     if transaction["operationAmount"]["currency"]["code"] == currency)
     return transaction_usd


if __name__ == "__main__":
    with open('transactions.txt', 'r', encoding='utf-8') as file:
        transactions = json.load(file)

    usd_transactions = filter_by_currency(transactions, "USD")
    for _ in range(3):
        print(next(usd_transactions))
