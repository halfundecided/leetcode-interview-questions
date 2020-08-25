#
# @lc app=leetcode id=482 lang=python3
#
# [482] License Key Formatting
#

# @lc code=start
class Solution:
    # Solution from Discussion: https://github.com/halfundecided?tab=repositories
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.upper().replace('-', '')
        size = len(S)
        
        if size % K == 0:
            s1 = K
        else:
            s1 = size % K
        
        ret = S[:s1]
        while s1 < size:
            ret = ret + '-' + S[s1:s1+K]
            s1 = s1 + K
            
        return ret
        
# @lc code=end

