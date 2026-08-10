class NumArray:
    arr = []
    def __init__(self, nums: List[int]):
        self.arr = nums

    def sumRange(self, left: int, right: int) -> int:
        res = 0
        for i in range(left,right+1):
            res += self.arr[i]
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
class NumArray:
    prefix_array = []
    def __init__(self, nums: List[int]):
        self.prefix_array = []
        prefix_sum = 0
        for i in nums:
            prefix_sum += i
            self.prefix_array.append(prefix_sum)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_array[right]
        else:
            return self.prefix_array[right] - self.prefix_array[left-1]
