#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
from collections import defaultdict


class Solution:
    # My 1st Solution
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = defaultdict(int)
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        for key in counts.keys():
            if counts[key] > 1:
                return True
        return False


"""
class Solution:
    # Kevin's Solution: https://www.youtube.com/watch?v=qg0CY00qJqI&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=6
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        return False
"""
# @lc code=end
