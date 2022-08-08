#https://leetcode.com/problems/valid-anagram/ -> SOLVED

def isAnagram(s, t):
    sChars = {}
    for char in s:
        if char in sChars:
            sChars[char] += 1
        else:
            sChars[char] = 1
    for char in t:
        if char in sChars:
            sChars[char] -= 1
        else:
            return False
    print(sChars)
    for key in sChars:
        if sChars[key] != False:
            return True
    return True

print(isAnagram("ab", "a"))