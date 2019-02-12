from datastructures.lists.node import DoublyLinkedNode

from . import list_helpers


def test_add_first():
    doubly_linked_list = list_helpers._populate_list(num=1, type_="doubly")

    assert doubly_linked_list.head.value == 0
    assert doubly_linked_list.tail.value == 0
    doubly_linked_list.add_first(DoublyLinkedNode(20))

    assert doubly_linked_list.head.value == 20
    assert doubly_linked_list.tail.prev.value == 20


def test_add_last():
    doubly_linked_list = list_helpers._populate_list(num=1, type_="doubly")
    assert doubly_linked_list.tail.value == 0
    assert doubly_linked_list.head.value == 0

    doubly_linked_list.add_last(DoublyLinkedNode(10))

    assert doubly_linked_list.tail.value == 10
    assert doubly_linked_list.tail.prev.value == 0


def test_remove_last():
    doubly_linked_list = list_helpers._populate_list(num=10, type_="doubly")
    assert doubly_linked_list.tail.value == 0
    assert doubly_linked_list.tail.prev.value == 1

    doubly_linked_list.remove_last()
    assert doubly_linked_list.tail.value == 1
    assert doubly_linked_list.tail.prev.value == 2
