from time import time


def timeit(func):
    def wrapper(*args, **kw):
        begin = time()
        func(*args, **kw)
        end = time()
        print(f'{func.__name__}: ', end - begin)
    return wrapper