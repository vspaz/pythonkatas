from datastructures.stack.balanced_brackets import is_brackets_balanced

some_string = "{([()])}{}"


def test_brackets_balanced():

    assert True is is_brackets_balanced(astring=some_string)


def test_bracket_unbalanced():
    assert False is is_brackets_balanced(astring=some_string[1:])


def test_empty_string():
    assert False is is_brackets_balanced(astring="gibberish")
