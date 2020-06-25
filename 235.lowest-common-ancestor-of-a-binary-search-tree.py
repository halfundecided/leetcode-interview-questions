#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# class Solution:
#     # My 1st Solution: get helped from discussion - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/discuss/65183/My-Python-recursive-solution
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if root == None or p == None or q == None:
#             return None
#         if (max(p.val, q.val) < root.val):
#             return self.lowestCommonAncestor(root.left, p, q)
#         elif (min(p.val, q.val) > root.val):
#             return self.lowestCommonAncestor(root.right, p, q)
#         else:
#             return root


class Solution:
    # Kevin's Solution: https://www.youtube.com/watch?v=kulWKd3BUcI&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=37
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


# @lc code=end
