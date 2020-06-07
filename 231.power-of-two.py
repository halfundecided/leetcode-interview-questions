#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start


class Solution:
    # My 1st Solution
    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        while i < 100:
            if 2 ** i == n:
                return True
            i += 1
        return False


"""
class Solution:
    # Kevin's Solution: https://www.youtube.com/watch?v=uVAvuyah9Ek&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=2
    def isPowerOfTwo(self, n: int) -> bool:
        i = 1
        while (i < n):
            i *= 2
        
        return i == n
"""
# @lc code=end
