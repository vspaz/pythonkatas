import math


def is_palindrome(x):
    if x <= 0:
        return False

    num_digits = math.floor(math.log10(x)) + 1
    num_of_tens = 10 ** num_digits
    for i in range(num_digits // 2):
        biggest_num = x // num_of_tens
        smallest_num = x % 10
        if smallest_num != biggest_num:
            return False
        x %= num_of_tens
        x //= 10
        num_of_tens //= 100
    return True


def is_alpha_numeric_palindrome(astring):
    string_len = len(astring)
    if string_len <= 1:
        return False
    for i in range(string_len // 2):
        if astring[i] != astring[-(i + 1)]:
            return False
    return True


if __name__ == "__main__":
    assert is_alpha_numeric_palindrome(astring="boofoob")
    assert not is_alpha_numeric_palindrome(astring="foobar")
    assert is_alpha_numeric_palindrome(astring="ofo")
    assert is_palindrome(111)
