#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
from collections import defaultdict


# class Solution:
#     # My 1st Solution: List Dictionary & Array for distances
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         dict = defaultdict(list)
#         for i in range(len(nums)):
#             if nums[i] in dict:
#                 dict[nums[i]].append(i)
#             else:
#                 dict[nums[i]] = [i]

#         distances = []
#         for indexes in dict.values():
#             if len(indexes) > 1:
#                 for i in range(0, len(indexes) - 1):
#                     distances.append(indexes[i + 1] - indexes[i])
#         if distances == []:
#             return False
#         if k in distances:
#             return True
#         else:
#             result = True
#             for i in distances:
#                 if i > k:
#                     result = False
#                     break
#             return result

class Solution:
    # A bit better Solution from Discussions: https://leetcode.com/problems/contains-duplicate-ii/discuss/61375/Python-concise-solution-with-dictionary.
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for index, value in enumerate(nums):
            if (value in dic) and (index - dic[value] <= k):
                return True
            dic[value] = index
        return False

# @lc code=end
