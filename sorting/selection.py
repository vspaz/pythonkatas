def selection_sort(array):
    array_size = len(array)
    for i in range(array_size):
        smallest_item_idx = i
        for j in range(i + 1, array_size):
            if array[j] < array[smallest_item_idx]:
                smallest_item_idx = j
        array[i], array[smallest_item_idx] = array[smallest_item_idx], array[i]
