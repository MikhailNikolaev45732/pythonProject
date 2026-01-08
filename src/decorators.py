from functools import wraps


def log(filename=None):
    """Декоратор для логирования"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f"Function: {func.__name__}. Result: {result}"
                if filename:
                    with open(filename, 'a') as f:
                        f.write(f"Function: {func.__name__}. Result: {result}\n")
                else:
                    print(log_message)
                return result
            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message)
                else:
                    print(log_message)

        return wrapper

    return decorator


@log(filename="mylog.txt")
@log()
def my_function(x, y):
    """Функция складывает аргументы полученные на вход"""
    return x + y

my_function(1, 2)
help(my_function)
