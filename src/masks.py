import requests
import os
import datetime
import logging
from venv import logger


"""Функция get_mask_card_number принимает на вход номер карты и возвращает
её маску
входной аргумент: 7000792289606361
выход функции: 7000 79** ****6361"""

# logging.basicConfig(
#     level=logging.INFO,
#     format='%(levelname)s:%(name)s:%(message)s'
# )

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/masks.log', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# logging.basicConfig(
#     filename='masks.log',
#     filemode='a+',
#     format='%(levelname)s:%(name)s:Request time: %(asctime)s',
#     level=logging.INFO
# )
#
#
# logger = logging.getLogger()


def get_mask_card_number(card_number: int) -> str:
    """Функция  принимает на вход номер карты и возвращает ее маску."""
    logger.info("Функция получает на вход номер карты")
    card_str = str(card_number)
    card_num_len = len(card_str)

    if card_num_len > 0 and card_num_len != 16:
        raise ValueError("Некорректный ввод номера")
    elif card_num_len == 0:
        raise ValueError("Введите номер")

    return card_str[:4] + " " + card_str[4:6] + "** ****" + card_str[-4:]


"""Функция get_mask_account принимает на вход номер счета и возвращает
   его маску
   входной аргумент: 73654108430135874305
   выход функции: **4305"""


def get_mask_account(account_number: int) -> str:
    """Функция  принимает на вход номер счета и возвращает его маску."""
    account_str = str(account_number)
    account_num_len = len(account_str)

    if account_num_len > 0 and account_num_len != 20:
        raise ValueError("Некорректный ввод номера")
    elif account_num_len == 0:
        raise ValueError("Введите номер")

    return "**" + account_str[-4:]

