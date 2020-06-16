#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
from collections import defaultdict


class Solution:
    # My 1st Solution
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = defaultdict(int)
        word2 = defaultdict(int)
        for i in s:
            if i in word1:
                word1[i] += 1
            else:
                word1[i] = 1
        for i in t:
            if i in word2:
                word2[i] += 1
            else:
                word2[i] = 1

        return word1 == word2
# @lc code=end
