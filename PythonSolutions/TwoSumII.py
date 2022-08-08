# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


def twoSum(numbers, target):
    l = 0  # left pointer
    r = len(numbers) - 1  # right pointer

    while numbers[l] + numbers[r] != target:  # or while l < r
        if numbers[l] + numbers[r] > target:
            r -= 1
        if numbers[l] + numbers[r] < target:
            l += 1

    return [numbers[l], numbers[r]]
