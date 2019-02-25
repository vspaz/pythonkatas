def get_max(a, b, c):
    return max([a, b, c])


def get_max2(a, b, c):
    maximum = a
    for i in (b, c):
        if i > maximum:
            maximum = i
    return maximum


def get_max3(a, b, c):
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    return maximum


if __name__ == "__main__":
    a, b, c = 5, 3, -5
    assert 5 == get_max(a, b, c) == get_max2(5, 3, 1) == get_max3(a, b, c)
