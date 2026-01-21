# import pytest
# import json
from unittest.mock import patch
from src.external_api import currency_conversion


@patch('requests.request')
def test_currency_conversion(mock_request):
    """@patch('requests.request') используется для замены функции requests.request на её макет,
     чтобы мы могли контролировать возвращаемые данные и не делать реальные запросы к API."""
    mock_request.return_value.json.return_value = {'result': None}
    result = currency_conversion("8221.37", "USD")
    assert result == None, "Конвертация валюты не прошла как ожидалось"
