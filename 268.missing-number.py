#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start


class Solution:
    # My 1st Solution
    def missingNumber(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        if nums == [0]:
            return 1
        for i in range(0, len(nums)+1):
            if i in nums:
                continue
            else:
                return i


# class Solution:
#     # Kevin's Solution: https://www.youtube.com/watch?v=YMYVYSWL93w&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=25
#     def missingNumber(self, nums: List[int]) -> int:
#         sum = 0
#         for i in nums:
#             sum += i
#         n = len(nums) + 1
#         return int((n * (n-1)/2) - sum)


# @lc code=end
