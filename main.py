from l2_two_pointers.p0088_merge_sorted_array import Solution

def main():
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    result = Solution().merge(nums1,m,nums2,n)
    print(result)

if __name__ == "__main__":
    main()