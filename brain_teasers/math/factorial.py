def factorial_iter(num):
    total = 1
    for i in range(1, num + 1):
        total *= i
    return total


def factorial_rec(num):
    if num <= 1:
        return 1
    return num * factorial_rec(num - 1)


if __name__ == "__main__":
    assert 120 == factorial_iter(num=5)
    assert 120 == factorial_rec(num=5)
