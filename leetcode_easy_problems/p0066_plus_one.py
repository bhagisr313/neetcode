class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        res = []
        sum = 0
        for i in digits[::-1]:
            sum = i + carry
            if sum >= 10:
                carry = 1
                sum = 0
            else:
                carry = 0
            res.append(sum)
        if carry == 1:
            res.append(carry)
        return res[::-1]
