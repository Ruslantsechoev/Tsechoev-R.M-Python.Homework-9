from typing import Callable
from time import sleep, strftime, localtime, time
from functools import wraps


def sleep_2s(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):

        print("Sleep - 2s")
        sleep(2.0)

        result = func(*args, **kwargs)
        return result

    return wrapper


@sleep_2s
def main():
    print(f"{strftime('%d-%m-%Y %H:%M:%S', localtime(time()))}")
    main()
    print(f"{strftime('%d-%m-%Y %H:%M:%S', localtime(time()))}")


if __name__ == '__main__':
    main()