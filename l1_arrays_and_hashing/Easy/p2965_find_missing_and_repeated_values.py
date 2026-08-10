class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        result = []
        my_set = set()
        length = len(grid)*len(grid)
        for element in grid:
            for i in element:
                if i not in my_set:
                    my_set.add(i)
                else:
                    result.append(i)
        for j in range(1,length+1):
            if j not in my_set:
                result.append(j)
        return result