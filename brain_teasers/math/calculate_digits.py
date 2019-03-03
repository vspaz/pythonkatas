import math


def get_digits(num):
    count = 0
    while num != 0:
        num //= 10
        count += 1
    return count


def get_digits2(num):
    return math.floor(math.log10(num)) + 1


if __name__ == "__main__":
    assert 4 == get_digits(num=1984)
    assert 4 == get_digits2(num=1984)
