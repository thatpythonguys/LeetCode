#https://leetcode.com/problems/longest-consecutive-sequence/
from msilib import sequence


def longestConsecutive(nums):
        """ Sorting the nums and then counting the length of consecutive sequences. O(n log n) since sorting is a O(n log n) operation.
        nums.sort()
        sequencelength = 0
        maxLength = 0

        for i in range(len(nums)):
            if i == 0:
                sequencelength += 1
            elif nums[i] == nums[i - 1]:
                continue
            elif nums[i] == nums[i - 1] + 1:
                sequencelength += 1
            else:
                if sequencelength > maxLength:
                    maxLength = sequencelength
                    sequencelength = 1

        if sequencelength > maxLength:
            maxLength = sequencelength
        return maxLength
        """
        nums = set(nums)
        maxLength = 0
        cursequence = 0
        for num in nums:
            if (num - 1) in nums: #checking if the number is the beginning of a sequence.
                continue
            else:
                cursequencelength = 0
                while num + cursequencelength in nums:
                    cursequencelength += 1
            maxLength = max(maxLength, cursequencelength)
        
        return maxLength
            


print(longestConsecutive([100,4,200,1,3,2]))
#testcases: [9,1,-3,2,4,8,3,-1,6,-2,-4,7] [] [100,4,200,1,3,2]
