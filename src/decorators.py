def log(filename=None):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            if filename:
                with open(filename, 'a') as f:
                    f.write(f"Function: {func.__name__}. Result: {result}\n")
            else:
                print(f"Function:{func.__name__}. Result: {result}")
            return result
        return wrapper
    return decorator


@log(filename="mylog.txt")
#@log()
def my_function(x, y):
    return x + y

my_function(1, 2)

