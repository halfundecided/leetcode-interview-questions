#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start


class Solution:
    # My 1st Solution
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = []
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for i in s:
            if i in brackets.keys():
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if i == brackets[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

# I think my solution is more efficient than Kevin's!
# @lc code=end
