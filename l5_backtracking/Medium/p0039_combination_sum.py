class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(i, subset):
            if sum(subset) >= target:
                if sum(subset) == target:
                    result.append(subset)
                return 
            dfs(i+1, subset.copy())
            subset.append(candidates[i])
            dfs(i+1, subset)
        dfs(0,[])
        return result