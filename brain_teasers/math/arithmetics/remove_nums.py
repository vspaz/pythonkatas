def removeElement(nums, val):
    if len(nums) <= 1:
        return len(nums)
    while val in nums:
        del nums[nums.index(val)]
    return len(nums)


if __name__ == "__main__":
    print(removeElement([2, 2, 3, 3], 2))
