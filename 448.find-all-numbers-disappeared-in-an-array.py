#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
# class Solution:
#     # My 1st Solution: TLE
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         if nums == [] or nums == None:
#             return []
#         result = []
#         for i in range(1, len(nums)+1):
#             if i not in nums:
#                 result.append(i)
        
#         return result

class Solution:
    # Solution from Discussion
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # For each number i in nums,
        # we mark the number that i points as negative.
        # Then we filter the list, get all the indexes
        # who points to a positive number
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
                
        
# @lc code=end

