# 496. Next Greater Element I
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_dict = {}
        result = []
        for i in range(0,len(nums2)-1):
            greaterfound = False
            for j in range(i+1,len(nums2)):
                if nums2[j] > nums2[i]:
                    greaterfound = True
                    my_dict[nums2[i]] = nums2[j]
                    break
        for k in nums1:
            result.append(my_dict.get(k,-1))
        return result