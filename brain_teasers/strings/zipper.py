

# an alternative solution would be to use functools.groupby.
def zipper(astring):
    if not astring:
        return
    if len(astring) == 1:
        return astring + str(len(astring))
    char_and_count = []
    prev = astring[0]
    count = 1
    for letter in astring[1:]:
        if letter == prev:
            count += 1
        else:
            char_and_count.append(prev + str(count))
            count = 1  # reset counter
        prev = letter
    char_and_count.append(prev + str(count))
    return "".join(char_and_count)


if __name__ == "__main__":
    assert "a1b1c7d5e4" == zipper("abcccccccdddddeeee")
