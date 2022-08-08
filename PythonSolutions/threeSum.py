# https://leetcode.com/problems/3sum/


def threeSum(nums):

    nums.sort()
    result = []
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            ThreeSum = a + nums[l] + nums[r]
            if ThreeSum > 0:
                r -= 1
            elif ThreeSum < 0:
                l += 1
            else:
                result.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return result


if __name__ == "__main__":
    print('hello')
