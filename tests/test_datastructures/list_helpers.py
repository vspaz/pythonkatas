from datastructures.lists.doubly_linked_list import DoublyLinkedList
from datastructures.lists.node import DoublyLinkedNode, SingleLinkedNode
from datastructures.lists.singly_linked_list import LinkedList

list_types = {
        "singly": LinkedList,
        "doubly": DoublyLinkedList,
    }

node_types = {
    "singly": SingleLinkedNode,
    "doubly": DoublyLinkedNode,
}


def _populate_list(num, type_="singly"):
    linked_list = list_types[type_]()
    for i in range(num):
        linked_list.add_first(node=node_types[type_](i))
    return linked_list
