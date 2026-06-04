class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        my_dict = dict()
        result = 0
        for i in str(n):
            my_dict[i] = my_dict.get(i,0) + 1
        for k, v in my_dict.items():
            result +=int(k) * v
        return result