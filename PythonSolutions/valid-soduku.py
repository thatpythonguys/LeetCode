# https://leetcode.com/problems/valid-sudoku/ -> SOLVED
from collections import Counter


def isValidSudoku(board):
    columnDict = {}
    rowDict = {}
    for i in range(9):  # initializing sets for each row and column
        rowDict[i] = set()
        columnDict[i] = set()
    for i in range(9):
        for j in range(9):
            curval = board[i][j]
            if curval == ".":
                continue
            if curval in rowDict[i] or curval in columnDict[j]:
                return False
            rowDict[i].add(curval)
            columnDict[j].add(curval)

    squaresDict = {}

    # classify each square by dividing indices by 3 and flooring.
    for i in range(3):
        for j in range(3):
            squaresDict[(i, j)] = set()

    for i in range(9):
        for j in range(9):
            square = ((i // 3), (j // 3))
            curval = board[i][j]
            if curval == ".":
                continue
            if curval in squaresDict[square]:
                return False
            squaresDict[square].add(curval)
    return True


print(isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
      "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
