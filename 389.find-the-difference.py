#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dicS = {}
        dicT = {}
        for i in range(len(s)):

            # @lc code=end
