#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
import re
class Solution:
    # My 1st Solution
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        stack = []
        cleanS = re.sub('[^A-Za-z0-9]+', '', s)
        cleanS = cleanS.lower()
        for i in cleanS:
            stack.append(i)
        for letter in cleanS:
            if stack.pop() != letter:
                return False
        
        return True
        
# @lc code=end

