#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from collections import defaultdict


class Solution:
    # Kevin's Solution: https://www.youtube.com/watch?v=Aql6zHkONek&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=12
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(int)
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
            dic[target-num] = i

# @lc code=end
