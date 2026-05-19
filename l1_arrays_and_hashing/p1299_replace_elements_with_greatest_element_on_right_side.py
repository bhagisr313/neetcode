#1299. Replace Elements with Greatest Element on Right Side
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = [-1 for i in range(0,len(arr))]
        max_number = -1
        for i in range(len(result)-2,-1,-1):
            if arr[i+1] > max_number:
                max_number = arr[i+1]
            result[i] = max_number
        return result
# initializing the result array with -1, iterating from backside taking max value and comparing the rest values and replacing with max value. 