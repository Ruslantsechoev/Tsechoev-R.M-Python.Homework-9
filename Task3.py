from functools import wraps
from typing import Callable



def counter(func: Callable):
    count = 0

    @wraps(func)
    def wrapper(*args, **kwargs):

        wrapper.count += 1
        result = func(*args, **kwargs)


        print(f"Function call - {wrapper.count}")
        return result

    wrapper.count = 0
    return wrapper


@counter
def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1): f *= i
    return f


def main() -> None:
    print(f"{factorial(10)}")
    print(f'{factorial(100)}')


if __name__ == '__main__':
    main()