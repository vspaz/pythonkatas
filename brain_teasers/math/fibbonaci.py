def fib(num):
    return num if num <= 1 else fib(num - 1) + fib(num - 2)


def fib_generator(num):
    a, b = 0, 1
    count = 0
    while count < num:
        yield a
        a, b = a + b, a
        count += 1


if __name__ == "__main__":
    for i in range(10):
        print(fib(i))

    for i in fib_generator(10):
        print(i)
