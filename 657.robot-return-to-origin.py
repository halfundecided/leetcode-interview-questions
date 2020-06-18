#
# @lc app=leetcode id=657 lang=python3
#
# [657] Robot Return to Origin
#

# @lc code=start


class Solution:
    # My 1st Solution: Naive Approach - O(N)
    def judgeCircle(self, moves: str) -> bool:
        location = [0, 0]
        for i in moves:
            if i == 'U':
                location[1] += 1
            if i == 'D':
                location[1] -= 1
            if i == 'L':
                location[0] -= 1
            if i == 'R':
                location[0] += 1

        return location == [0, 0]
# @lc code=end
