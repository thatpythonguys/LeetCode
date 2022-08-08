#https://leetcode.com/problems/product-of-array-except-self/description/

from itertools import product
from math import prod

"""" TOO SLOW. Time: O(n^2) time
def productExceptSelf(nums):
    ansDict = {}
    result = []
    for i in range(len(nums)):
        ansDict[i] = 1
    
    for i, num in enumerate(nums):
        for key in ansDict:
            if key != i:
                ansDict[key] *= num

    result = list(ansDict.values())
    return result
"""
def productExceptSelf(nums):
    #Crux of Problem: answer is the left product * right product.
    result = []
    prefix = 1

    for i in range(len(nums)): #calculate prefix product from left to right.
        result.append(prefix)
        prefix *= nums[i]

    #print(result)
    postfix = 1
    for i in range(len(nums) - 1, -1, -1): #calculate postfix product from right to left.
        result[i] *= postfix
        postfix *= nums[i]


    return result
    
print(productExceptSelf([1,2,3,4]))