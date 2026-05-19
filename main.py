from leetcode_easy_problems.p0028_find_the_index_of_the_first_occurance_in_a_string import Solution

def main():

    haystack = "aaa"
    needle = "aab"
    result = Solution().strStr(haystack,needle)
    print(result)

if __name__ == "__main__":
    main()