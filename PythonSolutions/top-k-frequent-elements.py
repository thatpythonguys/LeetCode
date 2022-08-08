#https://leetcode.com/problems/top-k-frequent-elements/ -> SOLVED

def topKFrequent(nums, k):
    elementDict = {}
    result = []
    for num in nums:
        if num in elementDict:
            elementDict[num] += 1
        else:
            elementDict[num] = 1
    
    temp = []
    for key, value in elementDict.items():
        temp.append([key, value])

    temp.sort(key = lambda x: x[1])
    print(temp)
    for i in range(k):
        result.append(temp[-1][0])
        temp.pop()
    return result


print(topKFrequent([1,1,1,2,2,3], 2))