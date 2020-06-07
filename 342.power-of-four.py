#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start


class Solution:
    # My 1st Solution
    def isPowerOfFour(self, num: int) -> bool:
        i = 1
        while (i < num):
            i *= 4

        if i == num:
            return True
        else:
            return False

# @lc code=end
