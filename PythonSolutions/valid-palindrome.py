# https://leetcode.com/problems/valid-palindrome/ -> SOLVED
from re import sub


def alphaNum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord(9))


def isPalindrome(s):
    """Requires extra memory and regex. Can we do it vanilla?
    s = s.lower() #O(n) time and O(n) space
    s = sub(r'[^a-zA-Z0-9]', '', s)
    s2 = s[::-1]
    return s == s2
    """
# Two-Pointer Solution: O(n) time and O(1) space.

    l = 0
    r = len(s) - 1

    while l < r:
        while l < r and not alphaNum(s[l]):
            l += 1
        while l < r and not alphaNum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
