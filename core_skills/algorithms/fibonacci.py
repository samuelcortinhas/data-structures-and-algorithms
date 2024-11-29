def fibonacci(n: int):
    # Time O(2^n), Memory O(2^n)
    if n == 2 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


class Fibonacci:
    # Time O(n), Memory O(n)
    def __init__(self):
        self.cache = {1: 1, 2: 1}

    def fibo(self, n):
        if n in self.cache:
            return self.cache[n]

        self.cache[n - 2] = self.fibo(n - 2)
        self.cache[n - 1] = self.fibo(n - 1)

        return self.fibo(n - 1) + self.fibo(n - 2)

    def __call__(self, n):
        return self.fibo(n)


if __name__ == "__main__":
    print(fibonacci(8))
    print(Fibonacci()(8))
