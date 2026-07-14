class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        my_dict = dict()
        for ele in nums:
            my_dict[ele] = my_dict.get(ele, 0) + 1
        print(my_dict)
        for key,value in my_dict.items():
            if value % 2 != 0:
                return False
        return True