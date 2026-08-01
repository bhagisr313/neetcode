class Solution:
    def customSortString(self, order: str, s: str) -> str:
        extra_char = ''
        result = ''
        my_dict = Counter(s)
        for char in s:
            if char not in order:
                extra_char += char
        for o in order:
            if o in s:
                result += o * my_dict[o]
        if extra_char:
            result += extra_char
        return result