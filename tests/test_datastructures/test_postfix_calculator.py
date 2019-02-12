from datastructures.stack.postfix_calculator import postfix_calculator


def test_postfix_calculator():
    assert 10 == postfix_calculator(expression="5 3 2 * + 1 -")
