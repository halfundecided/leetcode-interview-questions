#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start


# class Solution:
#     # My 1st Solution: TLE
#     def isUgly(self, num: int) -> bool:
#         if num == 1:
#             return True
#         if num < 1:
#             return False
#         d = 2
#         prime_factors = set()
#         prime = {2, 3, 5}
#         while num > 1:
#             if num % d == 0:
#                 prime_factors.add(d)
#                 num = num / d
#                 d -= 1
#             d += 1

#         differences = prime_factors - prime
#         if len(differences) == 0:
#             return True
#         else:
#             return False


class Solution:
    # Answer from Discussion: https://leetcode.com/problems/ugly-number/discuss/69305/My-python-solution
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False

        for x in [2, 3, 5]:
            while num % x == 0:
                num = num / x
        return num == 1

# @lc code=end
