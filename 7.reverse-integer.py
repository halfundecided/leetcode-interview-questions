#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start


class Solution:
    # My 1st Solution
    def reverse(self, x: int) -> int:
        output = ""
        strX = str(x)
        if x >= 0:
            for i in range(len(strX) - 1, -1, -1):
                output += strX[i]
            output = int(output)
            if (abs(output) > (2 ** 31 - 1)) or (abs(output)) > (1 << 31) - 1:
                return 0
            return output
        if x < 0:
            for i in range(len(strX)-1, 0, -1):
                output += strX[i]
            output = '-' + output
            output = int(output)
            if (abs(output) > (2 ** 31 - 1)) or (abs(output)) > (1 << 31) - 1:
                return 0
            return output


# @lc code=end
