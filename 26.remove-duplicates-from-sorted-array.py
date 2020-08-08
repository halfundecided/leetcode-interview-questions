#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    # Kevin's Solution: https://www.youtube.com/watch?v=zIHe2V5Py3U&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=45
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i+1]:
                nums[index] = nums[i+1]
                index += 1
                
        return index
        
# @lc code=end

