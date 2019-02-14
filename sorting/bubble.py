def bubble_sort(array):
    array_size = len(array)
    for i in range(array_size):
        for j in range(array_size - 1, i, -1):
            if array[j] < array[j - 1]:
                array[j - 1], array[j] = array[j], array[j - 1]
