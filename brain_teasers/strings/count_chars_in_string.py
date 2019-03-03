
def count_chars(astring):
    if len(astring) < 3:
        return
    counter = 0
    for i in astring[:-2]:
        counter += 1
        if counter == 99:
            counter = 0

    counter = str(0) + str(counter) if counter < 10 else str(counter)
    return astring[:-2] + counter


def count_chars2(astring):
    if len(astring) < 3:
        return
    first = int(astring[-2])
    second = int(astring[-1])

    for _ in astring[0:-2]:
        print(astring[:-2] + str(first) + str(second))
        if first == 9 == second:
            first = 0
            second = 0
        elif second == 9:
            second = 0
            first += 1
        else:
            second += 1


if __name__ == "__main__":
    print(count_chars(astring="foo" * 1734 + "00"))
    print(count_chars2(astring="hellodarknessmyoldfriend" * 5 + str(0) + str(0)))
