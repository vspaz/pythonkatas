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


if __name__ == "__main__":
    print(count_chars(astring="foo" * 1734 + "00"))
