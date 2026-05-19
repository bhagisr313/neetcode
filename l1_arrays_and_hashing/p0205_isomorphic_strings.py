# Isomorphic Strings
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        my_dict_s = {}
        my_dict_t = {}
        if len(s) == len(t):
            for i in range(0,len(s)):
                if s[i] not in my_dict_s:
                    my_dict_s[s[i]] = t[i]
                else:
                    if my_dict_s[s[i]] != t[i]:
                        return False
                if t[i] not in my_dict_t:
                    my_dict_t[t[i]] = s[i]
                else:
                    if my_dict_t[t[i]] != s[i]:
                        return False
            return (len(my_dict_s.keys()) == len(my_dict_t.keys()))
        else:
            return False