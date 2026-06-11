from l3_linked_list.p0026_merge_two_sorted_lists import Solution,ListNode

def main():
    
    list2 = ListNode(1,ListNode(3,ListNode(4,None)))
    result = Solution().mergeTwoLists(list1,list2)
    print(result)

if __name__ == "__main__":
    main()