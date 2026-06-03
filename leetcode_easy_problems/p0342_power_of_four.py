class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        arr = []
        for i in range(0,16):
            arr.append(pow(4,i))
        if n in arr:
            return True
        else:
            return False
        
# another solution 
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if (n & (n - 1)) == 0 and (n & 0x55555555) != 0:
            return True
        else:
            return False