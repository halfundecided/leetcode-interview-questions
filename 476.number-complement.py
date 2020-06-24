#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#

# @lc code=start


# class Solution:
#     # My 1st Solution
#     def findComplement(self, num: int) -> int:
#         binNum = bin(num)[2:]
#         compNum = ''
#         for i in binNum:
#             if i == '0':
#                 compNum += '1'
#             else:
#                 compNum += '0'

#         return int(compNum, 2)

class Solution:
    # Kevin's Solution: https://www.youtube.com/watch?v=oURSuMY4zSc&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=34
    def findComplement(self, num: int) -> int:
        result = 0
        power = 1
        while num > 0:
            result += ((num % 2) ^ 1) * power
            power <<= 1
            num >>= 1

        return result

# @lc code=end
