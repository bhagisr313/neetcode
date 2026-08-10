class Solution:
    def findLucky(self, arr: List[int]) -> int:
        my_dict = dict()
        for i in arr:
            my_dict[i] = my_dict.get(i,0)+1
        largest_lucky = -1
        for k, v in my_dict.items():
            if k == v and k > largest_lucky:
                largest_lucky = k
        return largest_lucky