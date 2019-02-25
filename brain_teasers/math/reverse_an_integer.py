

def reverse_int(integer):
    remainder = abs(integer)
    reversed_interger = 0
    while remainder:
        last_integer = remainder % 10
        reversed_interger = reversed_interger * 10 + last_integer
        remainder //= 10
    return -reversed_interger if integer < 0 else reversed_interger


if __name__ == "__main__":
    assert 51 == reverse_int(integer=15000)
    assert -51 == reverse_int(integer=-15000)
    assert 1010011 == reverse_int(integer=1100101)
