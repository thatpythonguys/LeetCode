# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices):
    """ Brute Force
    #Time Complexity: O(n^2)
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            maxProfit = max(maxProfit, prices[j] - prices[i])

    return maxProfit
    """
    # sliding window algorithm
    # Time Complexity: Linear Search: O(n)
    l = 0  # day that we buy
    r = 1  # day that we sell
    maxProfit = 0
    while r < len(prices):
        # if sell price lower than buy price, we instead buy at lower price.
        if prices[r] < prices[l]:
            l = r
            r += 1
        else:
            # otherwise just compute profit and compare to current max.
            maxProfit = max(prices[r] - prices[l], maxProfit)
            r += 1

    return maxProfit


print(maxProfit([7, 1, 5, 3, 6, 4]))
