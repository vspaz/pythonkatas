from searching.binary_search import binary_search


def test_binary_search():
    array = [-10, -5, 0, 0, 1, 10, 135, 150, 200, 200, 80000]
    assert binary_search(alist=array, target_item=150)
    assert binary_search(alist=array, target_item=-10)
