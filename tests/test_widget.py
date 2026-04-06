import pytest
from src.widget import mask_account_card
from src.widget import get_date_json


@pytest.mark.parametrize(
    "account_string, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** ****5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** ****6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("VisaClassic 6831982476737658", "VisaClassic 6831 98** ****7658"),
        ("VisaPlatinum 8990922113665229", "VisaPlatinum 8990 92** ****5229"),
        ("VisaPlatinum 8990922113665229", "VisaPlatinum 8990 92** ****5229"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(account_string, expected):
    assert mask_account_card(account_string) == expected


@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("2024-03-15T02:26:18.671407", "15.03.2024"),
        ("2022-04-30T02:26:18.671407", "30.04.2022"),
        ("2024-01-05T02:26:18.671407", "05.01.2024"),
        ("2025-11-12T02:26:18.671407", "12.11.2025"),
    ],
)
def test_get_date(date_string, expected):
    assert get_date_json(date_string) == expected


def test_get_date_invalid_input():
    with pytest.raises(ValueError):
        get_date_json("")
