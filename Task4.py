from functools import cache

@cache
def fibonacci(n: int) -> int:
    """Function Fibonacci"""
    print(f"Вычисляю Фибоначчи для ряда - {n}")
    fib1 = fib2 = 1
    for _ in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2

    return fib2

def main() -> None:
    print(f"{fibonacci(4) = }")
    print(f"{fibonacci(10) = }")
    print(f"{fibonacci(6) = }")
    print(f"{fibonacci(4) = }")
    print(f"{fibonacci(10) = }")


if __name__ == '__main__':
    main()



