#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from collections import defaultdict


class Solution:
    # My 1st Solution
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1

        for item in count.items():
            if item[1] > (len(nums) / 2):
                return item[0]


# @lc code=end
