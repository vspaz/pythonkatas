import functools
import logging
import sys
import time

params = {
        "stream": sys.stderr,
        "level": logging.INFO,
        "format": "%(asctime)s.%(msecs)03d %(levelname)s: %(message)s",
        "datefmt": "%Y-%m-%d %X"
    }

logging.basicConfig(**params)


def log(foo, bar):
    def wrapper(func):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            logging.info(foo)
            ret = func(*args, **kwargs)
            time.sleep(1)
            logging.info(bar)
            return ret

        return _wrapper

    return wrapper


@log(foo="before", bar="after")
def do_something():
    pass


if __name__ == "__main__":
    do_something()
