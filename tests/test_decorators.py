import pytest
from src.decorators import log, my_function
import os


@log(filename=None)
def test_my_function():
    """Тест декорируемой функции"""
    return x + y
    result = my_function(x, y)
    assert result == 3
@log(filename="test_log.txt")
def test_log():
    """Тест функции декоратора с параметром"""
    test_my_function()
    with open("test_log.txt", "r") as file:
     log_content = file.read()
    assert "Function: test_my_function. Result: 3\n" in log_content
    os.remove("test_log.txt")


@log()
def test_my_function():
    return x + y

def test_logging_to_console(capsys):
    """Тест функции с перехватом пораметров выводимых в консоль"""
    test_my_function(1 , 2)
    captured = capsys.readouterr()
    assert "test_my_function error: TypeError. Inputs: (1, 2), {}\n" in captured.out
