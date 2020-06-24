#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # My 1st Solution
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False

        return self.getSum(root, 0, sum)

    def getSum(self, node: TreeNode, currentSum: int, target: int) -> bool:
        if node == None:
            return False
        if node.left == None and node.right == None:
            if currentSum + node.val == target:
                return True
            else:
                return False
        else:
            currentSum += node.val
            return self.getSum(node.left, currentSum, target) or self.getSum(node.right, currentSum, target)


# class Solution:
#     # Kevin's Solution: https://www.youtube.com/watch?v=Hg82DzMemMI&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=32
#     def hasPathSum(self, root: TreeNode, sum: int) -> bool:
#         if root == None:
#             return False
#         elif (root.left == None) and (root.right == None) and (sum - root.val == 0):
#             return True
#         else:
#             return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)


# @lc code=end
