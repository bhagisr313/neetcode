class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        r = k
        my_dict = dict()
        for i in range(l,r+1):
            my_dict[blocks[i]] = my_dict.get(my_dict[blocks[i]],0)
        while(r < len(blocks)):
            my_dict[blocks[l]] -= 1
            l += 1
            r += 1
            if r < len(blocks):
                
