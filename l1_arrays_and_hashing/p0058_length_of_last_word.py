# 58. Length of Last Word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        if s[i] == " ":
            while i > 0 and s[i] == " ":
                i -= 1
        counter = 0
        while i >= 0 and s[i] != " ":
            counter += 1
            i -= 1
        return counter