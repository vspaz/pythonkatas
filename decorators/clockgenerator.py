import functools
import time


def clock_iterations(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        for item in func(*args, **kwargs):
            start = time.perf_counter()
            yield item
            end = time.perf_counter()
            print("elapsed time: {}".format(end - start))
    return wrapped


def clock_func_calls(func):
    count = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        count += 1
        print("func call {}: {}".format(count, end - start))
        return ret
    return wrapper


@clock_iterations
def dummy_generator():
    yield from range(100)


@clock_func_calls
def get_factorial(num):
    return 1 if num < 2 else get_factorial(num - 1)


if __name__ == "__main__":
    for i in dummy_generator():
        pass
    get_factorial(10)
