def get_first_max_num_idx(nums):
    assert nums
    max_idx = 0
    max_num = nums[0]
    for idx, num in enumerate(nums):
        if num > max_num:
            max_idx = idx
            max_num = num
    return max_idx


if __name__ == "__main__":
    assert 6 == get_first_max_num_idx(nums=[10, 2, -1, 20, 0, 16, 50, 50, 40, 1, 3, 6, 9, 11])

