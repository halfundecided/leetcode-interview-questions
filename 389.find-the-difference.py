#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start


# class Solution:
#     # My 1st Solution: Two dictionaries
#     def findTheDifference(self, s: str, t: str) -> str:
#         dicS = {}
#         dicT = {}
#         for i in range(len(s)):
#             if s[i] in dicS:
#                 dicS[s[i]] += 1
#             else:
#                 dicS[s[i]] = 1
#         for i in range(len(t)):
#             if t[i] in dicT:
#                 dicT[t[i]] += 1
#             else:
#                 dicT[t[i]] = 1

#         differences = set()
#         if len(dicT) >= len(dicS):
#             differences = dicT.items() - dicS.items()
#         else:
#             differences = dicS.items() - dicT.items()

#         return list(differences)[0][0]


from collections import defaultdict


class Solution:
    # Kevin's Solution: https://www.youtube.com/watch?v=Ds4Kvd_xn4w&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=21
    def findTheDifference(self, s: str, t: str) -> str:
        dicS = defaultdict(int)
        for i in s:
            if i in dicS:
                dicS[i] += 1
            else:
                dicS[i] = 1
        print(dicS)

        for i in t:
            if (i in dicS and dicS[i] == 0) or (i not in dicS):
                return i
            else:
                dicS[i] -= 1

        return ''


# @lc code=end
