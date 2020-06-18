#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start


class Solution:
    # My 1st Solution
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        stack = []
        for i in range(len(nums)):
            if nums[i] != 0:
                stack.append(nums[i])

        for i in range(len(nums)):
            if i >= len(stack):
                nums[i] = 0
            else:
                nums[i] = stack[i]

# class Solution:
#     # Kevin's Solution: https://www.youtube.com/watch?v=1PEncepEIoE&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=14
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         index = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[index] = nums[i]
#                 index += 1

#         for i in range(index, len(nums)):
#             nums[i] = 0


# @lc code=end
