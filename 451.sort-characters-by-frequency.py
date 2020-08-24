#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    # My 1st Solution
    def frequencySort(self, s: str) -> str:
        dic = {}
        result = ""
        for letter in s:
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1
        
        sortedDic = sorted(dic.items(), key=lambda kv: kv[1], reverse=True)
        
        for i in range(len(sortedDic)):
            letters = sortedDic[i][0] * sortedDic[i][1]
            result += letters
            
        return result
        
# @lc code=end

