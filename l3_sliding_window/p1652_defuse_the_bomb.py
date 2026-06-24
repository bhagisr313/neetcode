class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        l = 1
        r = k 
        result = []
        running_sum = 0
        if k == 0:
            return[0 for i in range(len(code))]                

        for i in range(l,r+1):
            running_sum += code[i]
        for j in range(0, len(code)):
            result.append(running_sum)
            r  += 1
            running_sum += code[r % len(code)]
            running_sum -= code[l % len(code)]
            l += 1
        return result