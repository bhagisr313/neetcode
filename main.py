from l1_arrays_and_hashing.p1684_count_the_number_of_consistent_sytings import Solution

def main():
    allowed = "ab"
    words = ["ad","bd","aaab","baa","badab"]
    result = Solution().countConsistentStrings(allowed,words)
    print(result)

if __name__ == "__main__":
    main()