# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                print(i, j)
                if nums[i] + nums[j] == target:
                    if i != j:

                        return [i, j]


sol = Solution()
nums = [2, 7, 9]

print(sol.twoSum(nums, 9))
