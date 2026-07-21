class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_value = ""
        for i in range(0,len(num)-2):
            j = i+3
            substring = num[i:j]
            if substring[0] == substring[1] and substring[0] == substring[2]:
                if not max_value:
                    max_value = substring
                else:
                    if int(substring) > int(max_value):
                        max_value = substring
        return max_value