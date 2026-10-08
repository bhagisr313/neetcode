from l2_stacks.Medium.p0946_validate_stack_sequences import Solution

def main():
    pushed = [1,2,3,4,5]
    popped = [4,3,5,1,2]
    result = Solution().validateStackSequences(pushed, popped)
    print(result)

if __name__ == "__main__":
    main()