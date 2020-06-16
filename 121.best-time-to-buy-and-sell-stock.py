#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start

import math


class Solution:
    # Kevin's Solution: https://www.youtube.com/watch?v=mj7N8pLCJ6w&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=7
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0  # how much money we made so far
        minimum = math.inf  # the smallest value we've seen
        for i in range(len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            else:
                # calculate the profit if we sell in that day
                maximum = max(maximum, prices[i] - minimum)
        return maximum
# @lc code=end
