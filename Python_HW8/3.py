def type_logger(func):
    def wrapper(*args):
        printer = ''
        res = func(*args)
        for arg in args:
            printer += f'{func.__name__}({arg}: {type(arg)}), '
        printer += f'function res type: {type(res)}, result: {res}.'
        print(printer)
        return res
    return wrapper


@type_logger
def calc_cube(*numbers):
    lst = []
    for number in numbers:
        lst.append(number ** 3)
    return lst


a = calc_cube(5, 3, 1)
