import math


def get_gcd(num1, num2):
    num1, num2 = abs(num1), abs(num2)
    min_num = min([num1, num2])
    for i in range(min_num, 0, -1):
        if num1 % min_num == 0 and num2 % min_num == 0:
            return i
    return 1


def get_gcd2(num1, num2):
    num1, num2 = abs(num1), abs(num2)
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1


def get_gcd3(num1, num2):
    while num1:
        num1, num2 = num2 % num1, num1
    return num2


def get_gcd4(num1, num2):
    if num2 == 0:
        return num1
    return get_gcd4(num2, num1 % num2)


if __name__ == "__main__":
    assert 4 == get_gcd(8, 4)
    assert 4 == get_gcd2(8, 4)
    assert 4 == get_gcd3(8, 4)
    assert 4 == get_gcd4(8, 4)
    assert 4 == math.gcd(8, 4)
