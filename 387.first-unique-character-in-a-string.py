#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
from collections import defaultdict


class Solution:
    # My 1st Solution
    def firstUniqChar(self, s: str) -> int:
        dic = defaultdict(int)
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1

        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
            else:
                continue
        return -1


# @lc code=end
