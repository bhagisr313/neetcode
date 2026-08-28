class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        visited = set()
        result_set = set()
        for l in range(0,len(s)-2):
            if s[l] not in visited:
                for r in range(len(s)-1, l + 1, -1):
                    if s[r] not in visited and s[l] == s[r]:
                        visited.add(s[l])
                        mid_visited = set()
                        for m in range(l+1, r):
                            if s[m] not in mid_visited:
                                pal = s[l] + s[m] + s[r]
                                mid_visited.add(m)
                                result_set.add(pal)
        return len(result_set)