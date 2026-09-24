class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        result = 0
        result_list = []
        count_dict = dict()
        for value in nums:
            count_dict[value] = count_dict.get(value, 0) + 1
        for k, v in count_dict.items():
            if v == 3:
                res = []
                for i in range(0,len(nums)):
                    if k == nums[i]:
                        res.append(i)
                result_list.append(res)
        print(result_list)
        for array in result_list:
            for m in range(0, len(array)-2):
                n = m + 1
                o = m + 2
                if (array[n] - array[m] == array[o] - array[n]):
                    result+=1
        return result