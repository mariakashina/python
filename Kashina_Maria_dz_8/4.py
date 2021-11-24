def val_checker(callback):
    def val(func):
        def wrapper(arg):
            if callback(arg) is True:
                result = func(arg)
            else:
                raise ValueError(':wrong value')
            return result

        return wrapper

    return val


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(-3))
