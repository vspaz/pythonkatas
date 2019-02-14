
nums = [1, 1, 2,2, 50, 60, 60, 60]


def remove_duplicates(nums):
    prev_num = nums[0]
    count = 0
    for i in nums[1:]:
        if i == prev_num:
            nums.pop(count)
            continue
        prev_num = i
        count += 1
    return nums


print(remove_duplicates(nums))
