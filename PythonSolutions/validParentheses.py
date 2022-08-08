# https://leetcode.com/problems/valid-parentheses/

def isValid(s):
    """method: 1. parse the string
               2. if open parentheses, add to stack.
               3. if closing parenthese, check if correct match and pop from stack.
               4. If, at the end, the length of stack is zero, return True  
    """

    checkMap = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in s:
        if char == '(' or char == '[' or char == '{':
            stack.append(char)
        else:  # if stack means checking if stack is empty.
            if stack and checkMap[char] == stack[-1]:
                stack.pop()
            else:
                return False

    return len(stack) == 0


print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
