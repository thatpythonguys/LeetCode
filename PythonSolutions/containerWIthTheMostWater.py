# https://leetcode.com/problems/container-with-most-water/


def maxArea(height):
    """ Time Complexity: O(n^2) - two for loops.
    numLines = len(height)
    maxArea = 0
    for i in range(numLines):
        for j in range(i + 1, numLines):
            area = (j - i) * (min(height[i], height[j]))
            maxArea = max(maxArea, area)

    return maxArea
    """
    # Time Complexity: Linear Search: O(n)
    l = 0
    r = len(height) - 1
    # start with the maximum width container
    maxArea = (r - l) * (min(height[l], height[r]))

    while l < r:
        # if the left bars height is less than the one before it, then there is no way that the container will hold more, so we skip it.
        if l != 0 and height[l] < height[l - 1]:
            l += 1
            continue
        # same logic for the right bar.
        elif r != (len(height) - 1) and height[r] < height[r + 1]:
            r -= 1
            continue

        else:
            area = (r - l) * (min(height[l], height[r]))
            maxArea = max(area, maxArea)
            # whichever one was lower height, we update the value.
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

    return maxArea


if __name__ == "__main__":
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(maxArea([2, 3, 4, 5, 18, 17, 6]))
