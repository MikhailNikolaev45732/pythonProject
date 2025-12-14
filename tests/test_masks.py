import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account


@pytest.mark.parametrize(
    "card_number, expected",
    [
        (4782495185648523, "4782 49** ****8523"),
        (7005236482571998, "7005 23** ****1998"),
        (9655482000214786, "9655 48** ****4786"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_invalid_len():
    with pytest.raises(ValueError):
        get_mask_card_number(0)


@pytest.mark.parametrize(
    "account_number, expected",
    [(47824951856485234578, "**4578"), (58917005236482571998, "**1998"), (86479655482000214786, "**4786")],
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected


def test_get_mask_account_invalid_len():
    with pytest.raises(ValueError):
        get_mask_account(0)
