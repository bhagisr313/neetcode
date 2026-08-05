class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ball_index = []
        res_arr = []
        for i in range(0,len(boxes)):
            if boxes[i] == '1':
                ball_index.append(i)
        for j in range(0,len(boxes)):
            result = 0
            for k in ball_index:
                result += abs(k - j)
            res_arr.append(result)
        return res_arr