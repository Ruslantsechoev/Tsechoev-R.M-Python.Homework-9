from functools import wraps
from typing import Callable

def how_are_you(func: Callable):
    @wraps(func)

    def user_answer(*args, **kwargs):

        input("Как дела? ")
        print("А у меня не очень! Ладно, держи свою функцию.")

        result = func(*args, **kwargs)

        return result

    return user_answer


@how_are_you
def main():
    print("<Тут что-топроисходит...>")


if __name__ == '__main__':
    main()