#from binarySearch import search


def searchMatrix(matrix, target):
    # Time Complexity: O(log m) + O(log n) = O(log n)
    l = 0
    r = len(matrix) - 1
    while l <= r:  # Run Binary search on the rows of the matrix.
        m = (r + l) // 2
        # if number between values in row, run binary search again.
        if matrix[m][0] <= target and target <= matrix[m][-1]:
            l, r = 0, len(matrix[m]) - 1
            while l <= r:
                n = (r + l) // 2
                if matrix[m][n] == target:
                    return True
                if target < matrix[m][n]:
                    r = n - 1
                elif target > matrix[m][n]:
                    l = n + 1
            return False

        # if the target is bigger than the biggest value, delete bottom half
        elif target > matrix[m][-1]:
            l = m + 1
        # if the target is smaller than smallest value in this row, delete top half.
        elif target < matrix[m][0]:
            r = m - 1
    return False


print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))

print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))

print(searchMatrix([[1, 3]], 3))
