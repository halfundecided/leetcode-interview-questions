#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    # My 1st Solution: Binary Search - O(logN)
    # Also Kevin's Solution: https://www.youtube.com/watch?v=SNDE-C86n88&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=17
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            mid = int(left + (right - left) / 2)
            if isBadVersion(mid) == True:
                right = mid
            else:
                left = mid + 1
        return left

# @lc code=end
