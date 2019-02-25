import math


def _get_solution(a, b, D):
    return (-b + D) / (2 * a)


def _get_root_of_discriminant(a, b, c):
    D = b * b - 4 * a * c
    if D < 0:
        return None
    return math.sqrt(D)


def get_solutions(a, b, c):
    if a == 0:
        return None, None
    D = _get_root_of_discriminant(a, b, c)
    if D:
        return _get_solution(a, b, D), _get_solution(a, b, -D)
    return None, None


if __name__ == "__main__":
    x1, x2 = get_solutions(2, 5, -7)
    assert 1 == x1
    assert -3.5 == x2
