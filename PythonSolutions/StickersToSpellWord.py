#https://leetcode.com/problems/stickers-to-spell-word/ -> UNSOLVED
from collections import Counter
def numSharedChars(s1, s2):
    return sum((Counter(s1) & Counter(s2)).values())

def minStickers(stickers, target) -> int:
    for char in target:
        temp = 0 #temporary variable; tracks whether we have found a sticker that contains this character from the target. If the character is none of the stickers, there is no solution.
        for sticker in stickers: 
            if char in sticker:
                temp = 1
        if temp == 0:
            return -1
    numStickers = 0
    while target != '':
        maxShared = 0
        bestSticker = 0
        for i in range(len(stickers)):
            currentWordSimilarity = numSharedChars(stickers[i],target)
            if currentWordSimilarity > maxShared:
                maxShared = currentWordSimilarity
                bestSticker = stickers[i]
        for char in bestSticker:
            target = target.replace(char, '', 1)
        numStickers += 1
    return numStickers

stickers = ["these","guess","about","garden","him"]
target = "atomher"
print(minStickers(stickers, target))