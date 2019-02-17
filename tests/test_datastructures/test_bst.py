from datastructures.trees.bst import BSTree


def _create_tree():
    tree = BSTree()
    tree.insert(10, 20)
    tree.insert(5, 5)
    tree.insert(15, 30)
    tree.insert(16, 60)
    tree.insert(13, 40)
    tree.insert(2, 10)
    tree.insert(3, 8)
    return tree


def test_insert():
    tree = _create_tree()
    assert 5 == tree.contains(5).data
    assert 2 == tree.contains(2).key


def test_remove():
    tree = _create_tree()
    assert 40 == tree.contains(13).data

    tree.remove(13)
    assert None is tree.contains(13)


def test_get_max():
    tree = _create_tree()
    assert 16 == tree.get_max().key


def test_get_min():
    tree = _create_tree()
    assert 2 == tree.get_min().key
