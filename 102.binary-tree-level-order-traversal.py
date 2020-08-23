#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     # My 1st Solution(Approach): Recursion - Failed with a few edge cases 
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         if root == None:
#             return []
#         result = [[root.val]]
#         if root.left == None and root.right == None:
#             return result
#         if root.left == None:
#             result.append([root.right.val])
#             result.append(self._recursion(root.right))
#         if root.right == None:
#             result.append([root.left.val])
#             result.append(self._recursion(root.left))
#         if root.left != None and root.right != None: 
#             result.append([root.left.val, root.right.val])
#             result.append(self._recursion(root.left))
#             result.append(self._recursion(root.right))
        
#         output = list(filter(None, result)) 
        
#         return output
        
        
#     def _recursion(self, node):
        
#         if node.left == None and node.right == None:
#             return 
        
#         sub = []
#         sub.append(node.left.val)
#         sub.append(node.right.val)
#         return sub


class Solution:
    # Kevin's Solution: https://www.youtube.com/watch?v=XZnWETlZZ14&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=55
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        
        if root == None:
            return result
        
        queue = deque()
        queue.append(root)
        
        while len(queue):
            size = len(queue)
            currentLevel = []
            for i in range(size):
                current = queue.popleft()
                currentLevel.append(current.val)
                if current.left != None:
                    queue.append(current.left)
                if current.right != None:
                    queue.append(current.right)
                    
            result.append(currentLevel)
                
        return result

# @lc code=end

