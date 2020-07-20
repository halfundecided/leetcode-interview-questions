#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
class Solution:
    # My 1st Solution
    def isMonotonic(self, A: List[int]) -> bool:
        flag = True 
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                flag = False 
        
        if flag == True:
            return True 
        
        flag = True 
        for i in range(len(A)-1):
            if A[i] < A[i+1]:
                flag = False
        
        if flag == True:
            return True 
        
        return False

# class Solution:
#     # Kevin's Solution: https://www.youtube.com/watch?v=wqgvE8X-2jk&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=43
#     def isMonotonic(self, A: List[int]) -> bool:
#         increasing = True
#         decreasing = True
#         for i in range(len(A) - 1):
#             if A[i] > A[i + 1]:
#                 increasing = False
        
#         for i in range(len(A) - 1):
#             if A[i] < A[i + 1]:
#                 decreasing = False

#         return increasing or decreasing
        
# @lc code=end

