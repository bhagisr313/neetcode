# 392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = len(t)
        i = 0
        j = 0
        if s == "":
            return True
        else:
            while l > 0:
                if i == len(s):
                    return True
                if s[i] == t[j]:
                    i+=1
                j+=1
                l-=1
        return True if i == len(s) else False