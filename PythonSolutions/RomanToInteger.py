#https://leetcode.com/problems/roman-to-integer/ -> SOLVED
#SOLVED

def romanToInt(s: str) -> int:

    valueDict = {"I": 1, "V": 5, "X":10, "L":50, "C":100, "D":500 ,"M":1000} #Numeric Value of each character
    ans = 0
    for i in range(len(s)):
        if i == len(s) - 1:
            ans += valueDict[s[i]] #for the last character just add its value

        elif valueDict[s[i]] < valueDict[s[i + 1]]: #if the character before is smaller, then you subtract from the total.
            ans -= valueDict[s[i]]
        else:
            ans += valueDict[s[i]] #otherwise just add the character's value.
    return ans

print(romanToInt("XXVII"))
