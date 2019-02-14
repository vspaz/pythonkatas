from sorting.bubble import bubble_sort
from sorting.selection import selection_sort
from sorting.insertion import insertion_sort


def test_bubble_sort():
    array = [1, 20, -3, 0, 1, 50, -100500, 10, 80, 9, 9]
    expected = [-100500, -3, 0, 1, 1, 9, 9, 10, 20, 50, 80]
    bubble_sort(array=array)
    assert expected == array


def test_selection_sort():
    array = [1, 20, -3, 0, 1, 50, -100500, 10, 80, 9, 9]
    expected = [-100500, -3, 0, 1, 1, 9, 9, 10, 20, 50, 80]
    selection_sort(array=array)
    assert expected == array


def test_insertion_sort():
    array = [1, 20, -3, 0, 1, 50, -100500, 10, 80, 9, 9]
    expected = [-100500, -3, 0, 1, 1, 9, 9, 10, 20, 50, 80]
    insertion_sort(array=array)
    assert expected == array
