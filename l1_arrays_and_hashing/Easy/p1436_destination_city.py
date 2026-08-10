class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source_set = set()
        for i in range(0,len(paths)):
            source_set.add(paths[i][0])
        for j in range(0,len(paths)):
            if paths[j][1] not in source_set:
                return paths[j][1]
