from l3_binary_search.p0035_search_insert_position import Solution

def main():
    
    nums = [1,3,5,6]
    target = 8
    result = Solution().searchInsert(nums,target)
    print(result)

if __name__ == "__main__":
    main()