#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start

"""
- BFS, Recursion 
Answer from Kevin Naughton Youtube
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == None or len(grid) == 0:
            return 0

        numIslands = 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == '1':
                    numIslands += self.dfs(grid, i, j)

        return numIslands

    def dfs(self, grid, i, j):
        if grid[i][j] == '0' or i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
            return 0

        grid[i][j] = '0'
        self.dfs(grid, i - 1, j)  # check above
        self.dfs(grid, i + 1, j)  # chech below
        self.dfs(grid, i, j - 1)  # check left
        self.dfs(grid, i, j + 1)  # check right

        return 1

# @lc code=end
