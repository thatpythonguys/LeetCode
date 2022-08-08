# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from operator import le


def lengthOfLongestSubstring(s):

    l = 0
    maxLength = 0
    currentstringSet = set()

    for r in range(len(s)):
        while s[r] in currentstringSet:
            currentstringSet.remove(s[l])
            l += 1
        currentstringSet.add(s[r])
        maxLength = max(maxLength, r - l + 1)
    return maxLength


print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
