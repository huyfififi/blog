def fibonacci(n: int) -> int:
    assert n >= 0

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:  # n >= 2
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(10):
    print(fibonacci(i))
