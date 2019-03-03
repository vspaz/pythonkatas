def reverse_int(num):
    reversed_num = 0
    if num < 0:
        num = -num
    while num != 0:
        last_digit = num % 10
        reversed_num = reversed_num * 10 + last_digit
        num //= 10

    return -reversed_num if num < 0 else reversed_num


if __name__ == "__main__":
    assert 4891 == reverse_int(num=-1984)
    assert 4891 == reverse_int(num=1984)
