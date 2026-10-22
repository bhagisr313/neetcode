class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        output_counter = 0
        i = 0
        j = 0
        while (i < len(g) and j < len(s)):
            if (g[i] <= s[j]):
                output_counter += 1
                i += 1
            j += 1
        return output_counter