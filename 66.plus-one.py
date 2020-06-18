#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start


# class Solution:
#     # My 1st Solution: Naive Approach, but beats 99%
#     def plusOne(self, digits: List[int]) -> List[int]:
#         string = ''
#         output = []
#         for i in digits:
#             string += str(i)
#         print(int(string))
#         result = int(string) + 1
#         for i in str(result):
#             output.append(i)
#         return output

class Solution:
    # Kevin's Solution: https://www.youtube.com/watch?v=_sls9AdBymI&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=16
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        result = [0] * (len(digits) + 1)
        result[0] = 1
        return result

# @lc code=end
