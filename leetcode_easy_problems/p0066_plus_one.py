class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = ""
        for i in digits:
            res += str(i) 
        int_res = int(res) + 1
        result = [int(i) for i in list(str(int_res))]
        return result
        
