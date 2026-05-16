# 290 Word Pattern
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        my_list = s.split(" ")
        my_dict_p = {}
        my_dict_s = {}
        if len(pattern) == len(my_list):
            for i in range(0,len(pattern)):
                if pattern[i] not in my_dict_p:
                    my_dict_p[pattern[i]] = my_list[i]
                else:
                    if my_dict_p[pattern[i]] != my_list[i]:
                        return False
                if my_list[i] not in my_dict_s:
                    my_dict_s[my_list[i]] = pattern[i]
                else:
                    if my_dict_s[my_list[i]] != pattern[i]:
                        return False
            return True
        else:
            return False