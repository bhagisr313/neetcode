class Solution:
    def arrangeCoins(self, n: int) -> int:
        low = 1
        high = n
        while(low <= high):
            mid = (low + high)//2
            numberOfCoins = mid * (mid + 1)/2
            if n > numberOfCoins:
                low = mid + 1
            elif n < numberOfCoins:
                high = mid - 1
            else:
                return mid
        return high
    


# another solution brute force
    class Solution:
    def arrangeCoins(self, n: int) -> int:
        step = 0
        count = 0
        while n > 0:
            step += 1
            n -= step
            if n >= 0:
                count += 1
            else:
                return count
        return count
