def reverse_intger(num):
    reversed_num = 0
    quotient = 1
    if num < 0:
        num = abs(num)
        quotient = -1

    while num > 0:
        remainder = num % 10
        reversed_num = reversed_num * 10 + remainder
        num //= 10

    return reversed_num * quotient
