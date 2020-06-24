#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start


class Solution:
    # My 1st Solution
    # Note: list.remove() method only removes the first appearance
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)


# class Solution:
#     # Kevin's Solution: https://www.youtube.com/watch?v=sRKByfozeEg&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=33
#     def removeElement(self, nums: List[int], val: int) -> int:
#         index = 0
#         for i in nums:
#             if i != val:
#                 nums[index] = i
#                 index += 1


#         return index


# @lc code=end
