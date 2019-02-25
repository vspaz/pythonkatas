def is_letter(letter):
    return ord("A") <= ord(letter) <= ord("z")


if __name__ == "__main__":
    assert is_letter("b")
    assert not is_letter("~")
