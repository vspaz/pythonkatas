def removeElement(nums: 'List[int]', val: 'int') -> 'int':
    if len(nums) <= 1:
        return len(nums)
    while val in nums:
        del nums[nums.index(val)]
    return len(nums)


print(removeElement([2, 2, 3, 3], 2))