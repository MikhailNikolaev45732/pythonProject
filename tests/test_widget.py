import pytest
from src.widget import mask_account_card
from src.widget import get_date


@pytest.mark.parametrize("account_string, expected", [
                                                 ("Maestro 1596837868705199", "Maestro 1596 83** ****5199"),
                                                 ("Счет 64686473678894779589", "Счет **9589"),
                                                 ("MasterCard 7158300734726758", "MasterCard 7158 30** ****6758"),
                                                 ("Счет 35383033474447895560", "Счет **5560"),
                                                 ("VisaClassic 6831982476737658", "VisaClassic 6831 98** ****7658"),
                                                 ("VisaPlatinum 8990922113665229", "VisaPlatinum 8990 92** ****5229"),
                                                 ("VisaPlatinum 8990922113665229", "VisaPlatinum 8990 92** ****5229"),
                                                 ("Счет 73654108430135874305", "Счет **4305")
                                                 ])

def test_mask_account_card(account_string, expected):
    assert mask_account_card(account_string) == expected
