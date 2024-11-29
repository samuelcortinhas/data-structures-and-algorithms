def factorial_rec(n: int):
    # Time O(n), Memeory O(n)
    if n == 1:
        return 1

    return n * factorial_rec(n - 1)


def factorial(n: int):
    # Time O(n), Memory O(1)
    out = 1
    while n > 1:
        out *= n
        n -= 1
    return out


if __name__ == "__main__":
    print(factorial_rec(5))
    print(factorial(5))
