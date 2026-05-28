class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        index = 0
        for i in columnTitle[::-1]:
            numeric_value = ord(i) - 64
            result += numeric_value * pow(26,index)
            index += 1
        return result