#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start


class Solution:
    # My 1st Solution: Array
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        if len(nums1) >= len(nums2):
            shorter = nums2
            longer = nums1
        else:
            shorter = nums1
            longer = nums2

        for i in range(len(shorter)):
            if shorter[i] in longer and shorter[i] not in output:
                output.append(shorter[i])

        return output

# @lc code=end
