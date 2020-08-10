#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    # My 1st Solution
    def addBinary(self, a: str, b: str) -> str:
        binSum = bin(int(a, 2) + int(b, 2))
        binSum = binSum.replace('0b', '')
        
        return str(binSum)

# @lc code=end

