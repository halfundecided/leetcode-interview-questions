#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    # Solution from Discussion: https://leetcode.com/problems/decode-ways/discuss/253018/Python%3A-Easy-to-understand-explanation-bottom-up-dynamic-programming
    def numDecodings(self, s: str) -> int:
        # Bottom Up DP Question
        if s == "":
            return 0
        dp = [0] * (len(s) + 1)
        
        # base case
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        
        for i in range(2, len(s) + 1):
            # one digit
            if int(s[i-1:i]) > 0 and int(s[i-1:i]) <= 9:
                dp[i] += dp[i - 1]
            # two digit
            if int(s[i-2:i]) >= 10 and int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[len(s)]
        
# @lc code=end

