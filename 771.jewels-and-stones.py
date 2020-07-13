#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
class Solution:
    # My 1st Solution
    def numJewelsInStones(self, J: str, S: str) -> int:
        num = 0
        for stone in S:
            if stone in J:
                num += 1
        return num
# @lc code=end

