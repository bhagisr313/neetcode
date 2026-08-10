from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        my_dict = Counter(nums)
        bucket = [[] for i in range(0, len(nums)+1)]
        for key, val in my_dict.items():
            bucket[val].append(key)
        for ele in range(len(bucket)-1,-1,-1):
            bucket_list_at_ele = bucket[ele]
            if bucket_list_at_ele:
                for buck_ele in bucket_list_at_ele:
                    result.append(buck_ele)
                    k-= 1
                if k<=0:
                    return result
        return result

# ============================================================
# RELATED EASY PROBLEM
# ============================================================
# Contains Duplicate
#
# Review this Easy problem first if you need to revisit
# the basic pattern behind this Medium problem.
# ============================================================
