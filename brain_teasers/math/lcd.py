import math


def get_lcd(num1, num2):
    min_num = min([num1, num2])
    for i in range(2, min_num + 1):
        if num1 % i == 0 and num2 % i == 0:
            return i
    return 1


def get_lcd2(num1, num2):
    return (num1 * num2) / math.gcd(num1, num2)


if __name__ == "__main__":
    assert 1 == get_lcd(3, 13)
    assert 3 == get_lcd2(21, 63)
