#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if digits == None or len(digits) == 0:
            return result
        telephone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        self.letterCombination_helper(0, "", digits, telephone, result)
        return result

    # Type of DFS
    def letterCombination_helper(self, index: int, current: str, digits: str, telephone: dict, result: List[str]) -> List[str]:
        # loop through telephone[digits[index]] -> [a, b, c]
        # inside the for loop, call recursive function
        # i.e. "2" -> "a" -> "3" -> "d", "e", "f"
        #             -> "b" -> "3" -> "d", "e", "f"

        if index == len(digits):
            result.append(current)
            return
        for i in telephone[digits[index]]:
            self.letterCombination_helper(
                index + 1, current+i, digits, telephone, result)


# @lc code=end
