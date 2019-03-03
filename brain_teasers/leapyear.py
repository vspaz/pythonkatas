def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


if __name__ == "__main__":
    assert is_leap_year(year=1996)
