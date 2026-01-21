# import pytest
# import json
from unittest.mock import patch, mock_open
from src.utils import get_transaction_data


mock_data = mock_open(read_data='[{"id": 123, "currency": {"code": "RUB", "amount": 1000}}]')


@patch('builtins.open', mock_data)
def test_get_transaction_data():
    """Тестирование функции get_transaction_data с использованием заглушки mock_data и использованием для её
     создания mock_open из библиотеки mock """
    assert get_transaction_data('data/operations.json') == [{"id": 123, "currency": {"code": "RUB", "amount": 1000}}]
    mock_data.assert_called_once_with('data/operations.json', 'r', encoding='utf-8')
