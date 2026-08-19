class Solution:
    def maxScore(self, s: str) -> int:
        left_score, right_score = s[0].count('0'), s[1:].count('1')
        cur_total = left_score + right_score
        max_sum = cur_total
        for i in range(1, len(s)-1):
            if s[i] == '0':
                cur_total += 1
            else:
                cur_total -=1 
            max_sum = max(max_sum, cur_total)
        return max_sum