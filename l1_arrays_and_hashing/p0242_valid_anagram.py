# 242. Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}

        if len(s) != len(t):
            return False
        else:
            for i in s:
                if i in my_dict:
                    my_dict[i] += 1
                else:
                    my_dict[i] = 1
            for j in t:
                if j in my_dict:
                    my_dict[j] -= 1
                else:
                    return False
            for k,v in my_dict.items():
                if v != 0:
                    return False
        return True
# compared the length before processing, kept adding the character to disctionary, for the first string and removing the character for second string, if any char is not found return false in else. In last iterate through dict and check if the value is true for all keys, if not return false annd return true in the end outside the for loops. /// can use, counter(s) == counter(t) for one line code.
