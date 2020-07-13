#
# @lc app=leetcode id=693 lang=python3
#
# [693] Binary Number with Alternating Bits
#

# @lc code=start
# class Solution:
#     # My 1st Solution
#     def hasAlternatingBits(self, n: int) -> bool:
#         binary = bin(n).replace("0b", "")
#         if binary == '0' or binary == '1':
#             return True
#         for i in range(0, len(binary)-1):
#             if binary[i] == binary[i+1]:
#                 return False      
#         return True
        
class Solution:
    # Kevin's Solution: https://www.youtube.com/watch?v=9QFBqtvip9E&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=39
    def hasAlternatingBits(self, n: int) -> bool:
        last = n % 2
        n >>= 1
        while n > 0:
            current = n % 2
            if current == last:
                return False
            last = current
            n >>= 1
        return True 
        
        
# @lc code=end

