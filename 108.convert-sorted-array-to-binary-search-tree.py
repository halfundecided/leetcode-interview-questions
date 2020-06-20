#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # Kevin's Solution: https://www.youtube.com/watch?v=PZYTs9y4f4o&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=22
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums == None or len(nums) == 0:
            return None

        def constructBSTRecursive(nums, left, right):
            if left > right:
                return None

            mid = int(left + (right - left) / 2)
            current = TreeNode(nums[mid])
            current.left = constructBSTRecursive(nums, left, mid - 1)
            current.right = constructBSTRecursive(nums, mid + 1, right)

            return current

        return constructBSTRecursive(nums, 0, len(nums) - 1)

# @lc code=end
