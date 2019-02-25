from datastructures.lists.node import SingleLinkedNode
from datastructures.lists.singly_linked_list import LinkedList

from . import list_helpers


def _assert_values(linked_list, count, head_value=None, tail_value=None):
    assert linked_list.count == count
    if head_value:
        assert linked_list.head.value == head_value
    if tail_value:
        assert linked_list.tail.value == tail_value


def test_add_first():
    linked_list = LinkedList()
    _assert_values(linked_list, count=0)

    linked_list.add_first(SingleLinkedNode(value=10))
    _assert_values(linked_list, count=1, head_value=10, tail_value=10)

    linked_list.add_first(SingleLinkedNode(value=20))
    _assert_values(linked_list, count=2, head_value=20, tail_value=10)


def test_add_last():
    linked_list = LinkedList()
    _assert_values(linked_list, count=0)

    linked_list.add_last(SingleLinkedNode(value=10))
    _assert_values(linked_list, count=1, head_value=10, tail_value=10)

    linked_list.add_last(SingleLinkedNode(value=20))
    _assert_values(linked_list, count=2, head_value=10, tail_value=20)


def test_remove_first():
    linked_list = list_helpers._populate_list(num=10)
    _assert_values(linked_list, count=10, head_value=9, tail_value=0)

    linked_list.remove_first()
    _assert_values(linked_list, count=9, head_value=8, tail_value=0)


def test_remove_last():
    linked_list = list_helpers._populate_list(num=2)
    _assert_values(linked_list, count=2, head_value=1, tail_value=0)

    linked_list.remove_last()
    _assert_values(linked_list, count=1, head_value=1, tail_value=1)

    linked_list.remove_last()
    _assert_values(linked_list, count=0)


def test_remove():
    linked_list = list_helpers._populate_list(num=3)
    _assert_values(linked_list, count=3, head_value=2, tail_value=0)
    linked_list.remove(value=2)
    _assert_values(linked_list, count=2, head_value=1, tail_value=0)


def test_enumerate():
    linked_list = list_helpers._populate_list(num=3)
    list_values = linked_list.enumerate()
    assert 2 == next(list_values)
    assert 1 == next(list_values)
    assert 0 == next(list_values)
    assert None is next(list_values, None)


def test_empty_enumerate():
    linked_list = list_helpers._populate_list(num=0)
    list_values = linked_list.enumerate()
    assert None is next(list_values, None)


def test_contains():
    linked_list = list_helpers._populate_list(10)
    assert not linked_list.contains(10)
    assert linked_list.contains(5)


def test_reverse():
    linked_list = list_helpers._populate_list(10)
    for i in linked_list.enumerate():
        print(i)
    linked_list.reverse()
    for i in linked_list.enumerate():
        print(i)
