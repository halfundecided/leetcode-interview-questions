#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     # My 1st Solution: Wrong Answer 
#     def sumOfLeftLeaves(self, root: TreeNode) -> int:
#         # does this node have a left child? and is that left child a leaf
#         if root == None:
#             return 0

#         sum = 0
#         self.sumOfLeftLeavesRecursion(root, sum)

#         return sum

#     def sumOfLeftLeavesRecursion(self, current: TreeNode, sum: int) -> int:
#         if current.left != None and current.left.left == None and current.left.right == None:
#             sum += current.left.val
        
#         self.sumOfLeftLeavesRecursion(current.left, sum)
#         self.sumOfLeftLeavesRecursion(current.right, sum)


class Solution:
    # Kevin's Solution: https://www.youtube.com/watch?v=_gnyuO2uquA&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=44
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root == None:
            return 0
        elif root.left != None and root.left.left == None and root.left.right == None:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

# @lc code=end

