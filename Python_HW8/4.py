def val_checker(lambda_func):
    def decorator_func(func):
        def wrapper(*args):
            for arg in args:
                if not lambda_func(arg):
                    raise ValueError(f'wrong val: {arg}')
            res = func(*args)
            print(res)
            return res

        return wrapper
    return decorator_func


@val_checker(lambda x: x > 0)
def calc_cube(*numbers):
    lst = []
    for number in numbers:
        lst.append(number ** 3)
    return lst


calc_cube(5, 3, -4)
