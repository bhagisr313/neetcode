from l3_sliding_window.p2379_minimum_recolors_to_get_K_consecutive_black_blocks import Solution

def main():
    blocks = "WBBWWBBWBW"
    k = 7
    result = Solution().minimumRecolors(blocks,k)
    print(result)

if __name__ == "__main__":
    main()