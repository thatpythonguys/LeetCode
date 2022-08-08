from collections import Counter


def numSharedChars(s1, s2):
    return sum((Counter(s1) & Counter(s2)).values())

#print(numSharedChars("carrs", "rr"))
#l1 = [4,5,6]
# print(l1[-1:])

#nums = {(1,2): 3}
#s = "helloworld"
# print("hellowworld"[::-1]) reverse string


nums = [1, 3, 2]
nums.sort()
print(nums)
print(1 // 2)
