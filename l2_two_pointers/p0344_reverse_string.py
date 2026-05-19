# Reverse String
class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(0,len(s)//2):
            j = (len(s) - i) - 1
            temp = s[i]
            s[i] = s[j]
            s[j] = temp