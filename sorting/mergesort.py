def merge_sort(a_list):
    if len(a_list) > 1:  # check if it's a base case; the base case is 1 or 0
        mid = len(a_list) // 2
        left_half = a_list[: mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        left_idx = right_idx = unsplit_list_idx = 0

        while left_idx < len(left_half) and right_idx < len(right_half):
            if left_half[left_idx] < right_half[right_idx]:
                a_list[unsplit_list_idx] = left_half[left_idx]
                left_idx += 1
            else:
                a_list[unsplit_list_idx] = right_half[right_idx]
                right_idx += 1
            unsplit_list_idx += 1

        while left_idx < len(left_half):
            a_list[unsplit_list_idx] = left_half[left_idx]
            left_idx += 1
            unsplit_list_idx += 1

        while right_idx < len(right_half):
            a_list[unsplit_list_idx] = right_half[right_idx]
            right_idx += 1
            unsplit_list_idx += 1


a_list = [54, 26, 93, 17, 77, 31, 44, 44, 20]
merge_sort(a_list)
print(a_list)
