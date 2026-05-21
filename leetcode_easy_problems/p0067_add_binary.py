class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) -1
        j = len(b) -1
        max_len = max(i,j)
        sum = 0
        carry = 0
        res = ""
        while ( max_len >= 0):
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0
            if carry == 0:
                sum = bit_a ^ bit_b 
                carry = bit_a & bit_b
            else:
                sum = (bit_a ^ bit_b) ^ 1
                carry = bit_a | bit_b
            res += str(sum)
            i -= 1
            j -= 1
            max_len -= 1
        if carry == 1:
            res += str(carry)
        return res[::-1]