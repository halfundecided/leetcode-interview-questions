#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start


class Solution:
    # Kevin's Solution: https://www.youtube.com/watch?v=o8S2bO3pmO4&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=1
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
