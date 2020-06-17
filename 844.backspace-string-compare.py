#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start


class Solution:
    # My 1st Solution
    def backspaceCompare(self, S: str, T: str) -> bool:
        stackS = []
        stackT = []
        for i in range(len(S)):
            if S[i] == '#':
                if stackS == []:
                    continue
                stackS.pop()
            else:
                stackS.append(S[i])
        for i in range(len(T)):
            if T[i] == '#':
                if stackT == []:
                    continue
                stackT.pop()
            else:
                stackT.append(T[i])

        return stackS == stackT


# @lc code=end
