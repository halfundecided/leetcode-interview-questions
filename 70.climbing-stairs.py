#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start


class Solution:
    # My 1st Solution: David's help
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        arr = [0] * (n + 1)
        arr[1] = 1
        arr[2] = 2
        for i in range(3, n + 1):
            arr[i] = arr[i - 1] + arr[i - 2]
        return arr[n]

# @lc code=end
