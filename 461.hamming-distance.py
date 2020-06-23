#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#

# @lc code=start


# class Solution:
#     # My 1st Solution
#     def hammingDistance(self, x: int, y: int) -> int:
#         difference = bin(x ^ y)
#         output = 0
#         for i in difference:
#             if i == "1":
#                 output += 1
#         return output


class Solution:
    # Kevin's Solution: https://www.youtube.com/watch?v=oGU1At1GFvc&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=29
    def hammingDistance(self, x: int, y: int) -> int:
        result = 0
        while x > 0 or y > 0:
            # Gives last digit of binary number
            result += (x % 2) ^ (y % 2)
            # Shift
            x >>= 1
            y >>= 1

        return result


# @lc code=end
