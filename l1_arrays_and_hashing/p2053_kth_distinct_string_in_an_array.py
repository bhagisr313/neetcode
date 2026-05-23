class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        my_dict = dict()
        for element in arr:
            my_dict[element] = my_dict.get(element,0) + 1
        for i in arr:
            if my_dict[i] == 1:
                k -= 1
                if k == 0:
                    return i
        return ""