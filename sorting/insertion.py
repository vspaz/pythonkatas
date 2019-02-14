def insertion_sort(array):
    for i in range(1, len(array)):
        current = array[i]
        j = i
        while j > 0 and current < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = current
