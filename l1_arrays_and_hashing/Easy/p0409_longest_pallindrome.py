class Solution:
    def longestPalindrome(self, s: str) -> int:
        max_length = 0
        odd_flag = False
        pallindrome_dict = dict()
        for char in s:
            pallindrome_dict[char] = pallindrome_dict.get(char, 0) + 1
        for k, v in pallindrome_dict.items():
            if v % 2 == 0:
                max_length += v
            elif v % 2 == 1:
                max_length += (v-1)
                odd_flag = True
        if odd_flag:
            max_length += 1
        return max_length