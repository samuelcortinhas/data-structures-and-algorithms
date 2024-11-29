def fibonacci(n: int):
    if n == 2 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci(8))
