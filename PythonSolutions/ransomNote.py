#https://leetcode.com/problems/ransom-note/ -> SOLVED

def Check(ransomNote, magazine):
    ransomNote = list(ransomNote)
    magazine = list(magazine)

    for char in ransomNote:
        if char in magazine:
            magazine.remove(char)
            print(magazine)
        else:
            return False
    return True

ransomNote = input("ransomnote: ")
magazine = input("magazine: ")

print(Check(ransomNote, magazine))