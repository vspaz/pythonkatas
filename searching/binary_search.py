def binary_search_iterative(alist, target):
    low = 0
    upper = len(alist) - 1
    while low <= upper:
        mid = (low + upper) // 2
        mid_item = alist[mid]
        if mid_item == target:
            return True
        elif mid_item < target:
            low = mid - 1
        else:
            upper = mid + 1

    return False


def binary_serach_recursive(alist, target):
    if not alist:
        return
    mid = len(alist) // 2
    mid_item = alist[mid]
    if mid_item == target:
        return True
    if mid_item < target:
        return binary_serach_recursive(alist[mid + 1:])
    else:
        binary_serach_recursive(alist[:mid], target)
