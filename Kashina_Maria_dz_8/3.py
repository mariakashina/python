def type_logger(func):
    types = {}

    def wrapper(*args):
        for arg in args:
            types[arg] = type(arg)
        types1 = str(types).strip('{}')
        result = f'{func.__name__}({types1})'
        return result

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube(3, 4, 5))
