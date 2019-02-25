

num = int(input("please input num: \n"))
m = int(input("please input m: \n"))
nums = [None for _ in range(num)]
used = [False for _ in range(num)]


def union(idx):
    if idx == num:
        print(nums)
        return
    for i in range(m):
        nums[idx] = i
        union(idx + 1)


union(0)

print("================================")


def perms(idx):
    if idx == num:
        print(nums)
        return
    for i in range(m):
        if used[i]:
            continue
        nums[idx] = i
        used[i] = True
        perms(idx + 1)
        used[i] = False


perms(0)
