#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
from collections import defaultdict


class Solution:
    # My 1st Solution: Sorting algorithm
    # I didn't want to use bit-manipulation
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # nums = self.insertionSort(nums)
        nums.sort()  # in-place sorting algorithm I guess
        for i in range(0, len(nums), 3):
            if i == len(nums) - 1 and nums[i] != nums[i - 1]:
                return nums[i]

            if nums[i] != nums[i + 1]:
                return nums[i]

    # def insertionSort(self, arr):
    #     for i in range(1, len(arr)):
    #         key = arr[i]
    #         j = i - 1
    #         while j >= 0 and key < arr[j]:
    #             arr[j + 1] = arr[j]
    #             j -= 1
    #         arr[j + 1] = key
    #     return arr

# @lc code=end
