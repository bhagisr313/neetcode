# 605 Can Place Flowers
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        morphed_bed = [0,*flowerbed,0]
        for i in range(1,len(morphed_bed)-1):
            if morphed_bed[i-1] == 0 and morphed_bed[i] == 0 and morphed_bed[i+1] == 0:
                morphed_bed[i] = 1
                n -= 1
        return True if n <= 0 else False