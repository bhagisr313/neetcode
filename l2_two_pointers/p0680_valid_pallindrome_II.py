class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while(l < r):
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if s[l:r] == s[r-len(s)-1:l-len(s)-1:-1]:
                    return True
                elif s[l+1:r+1] ==  s[r-len(s):l-len(s):-1]:
                    return True
                return False
        return True