def is_palindrome(self, x: 'int') -> 'bool':
    if x < 0:
        return False
    temp = x
    reversed_num = 0
    while x > 0:
        remainder = x % 10
        reversed_num *= 10
        reversed_num += remainder
        x //= 10

    return reversed_num == temp
