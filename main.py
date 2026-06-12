from l3_linked_list.p0203_remove_linked_list_elements import Solution,ListNode

def main():
    
    list2 = ListNode(7,ListNode(7,ListNode(7,ListNode(7,None))))
    val = 7
    result = Solution().removeElements(list2, val)
    print(result)

if __name__ == "__main__":
    main()