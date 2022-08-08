# https://leetcode.com/problems/binary-search/


def search(nums, target):

    l = 0
    r = len(nums) - 1
    while l <= r:
        curIndex = (r + l) // 2  # this is the middle of the list.
        # curIndex = l + (r - l) // 2. In other languages, the above method can cause integer overflow. To resolve, this method works better.
        if nums[curIndex] == target:
            return nums[curIndex]
        if nums[curIndex] > target:
            r = curIndex - 1
        elif nums[curIndex] < target:
            l = curIndex + 1
    return -1


print(search([-1, 0, 3, 5, 9, 12], 9))
print(search([-1, 0, 3, 5, 9, 12], 2))
