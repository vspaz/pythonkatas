from datastructures.stack.stack import StackArray, StackList


def _assert_stack(stack):
    assert stack.is_empty()

    stack.push(10)
    stack.push(20)
    assert 2 == stack.size()
    assert 20 == stack.peek()

    assert 20 == stack.pop()
    assert 1 == stack.size()
    assert 10 == stack.peek()

    assert stack.pop()
    assert stack.is_empty()


def test_stack_array():
    _assert_stack(stack=StackArray())


def test_stack_list():
    _assert_stack(stack=StackList())
