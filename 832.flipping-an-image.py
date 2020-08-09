#
# @lc app=leetcode id=832 lang=python3
#
# [832] Flipping an Image
#

# @lc code=start
class Solution:
    # My 1st Solution
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            A[i].reverse()
            for j in range(len(A[i])):
                if A[i][j] == 0:
                    A[i][j] = 1
                else:
                    A[i][j] = 0
        return A

# @lc code=end

