#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start


# class Solution:
#     # My 1st Solution: Recursion
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         if len(s) == 0:
#             return

#         self.reverse_helper(s, 0, len(s)-1)

#     def reverse_helper(self, arr, index1, index2):
#         if index1 >= index2:
#             return
#         else:
#             temp = arr[index1]
#             arr[index1] = arr[index2]
#             arr[index2] = temp
#             self.reverse_helper(arr, index1 + 1, index2 - 1)

class Solution:
    # My 2nd Solution: Binary Search - runtime faster
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while (i < j):
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

# @lc code=end
