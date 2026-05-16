# 14. Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min([len(i) for i in strs])
        string_result = ""
        for i in range(0, min_length):
            char_at_i = strs[0][i]
            for j in range(0,len(strs)):
                if char_at_i != strs[j][i]:
                    return string_result
            string_result += char_at_i
        return string_result