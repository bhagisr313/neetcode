class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        r = k - 1
        length = len(blocks)
        my_dict = {
            "W" : 0,
            "B" : 0
        }
        for i in range(l,r+1):
            my_dict[blocks[i]] = my_dict.get(blocks[i],0) + 1
        min_counter = my_dict["W"]
        while(r < length):
            r += 1
            if r == length:
                break
            my_dict[blocks[r]] += 1
            my_dict[blocks[l]] -= 1
            l += 1
            min_counter = min(min_counter, my_dict["W"])

        return min_counter