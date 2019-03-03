import math


def is_palindrome(num):
    if num <= 0:
        return False
    digits_count = math.floor(math.log10(num)) + 1
    mid = digits_count // 2
    denominator = 10 ** (digits_count - 1)
    for i in range(mid):
        first = num // denominator
        last = num % 10

        if first != last:
            return False

        num %= denominator  # remove first digit
        num //= 10  # remove last digit
        denominator //= 100  # drop 2 digits
    return True


if __name__ == "__main__":
    assert is_palindrome(111)
    assert is_palindrome(22322)
    assert is_palindrome(1001001)
