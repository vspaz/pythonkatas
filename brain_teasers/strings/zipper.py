

# an alternative solution would be to use functools.groupby.
def zipper(astring):
    if not astring:
        return
    if len(astring) == 1:
        return astring + str(len(astring))
    char_and_count = []
    char = prev = astring[0]
    count = 1
    for letter in astring[1:]:
        if letter == char:
            prev = char
            count += 1
        else:
            char_and_count.append(prev + str(count))
            char = prev = letter
            count = 1
    char_and_count.append(char + str(count))
    return "".join(char_and_count)


if __name__ == "__main__":
    assert "a1b1c7d5e4" == zipper("abcccccccdddddeeee")
