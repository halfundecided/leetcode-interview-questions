#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
from collections import defaultdict


class Solution:
    # My 1st Solution
    def singleNumber(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for elem in dic:
            if dic[elem] == 1:
                return elem

# @lc code=end
