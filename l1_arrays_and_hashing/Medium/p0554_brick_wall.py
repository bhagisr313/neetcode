class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        max_length = len(wall)
        my_dict = dict()
        max_value = 0
        for row in wall:
            prefix_sum = 0
            for brick in row[:-1]:
                prefix_sum += brick
                my_dict[prefix_sum] = my_dict.get(prefix_sum, 0) + 1
        for k, v in my_dict.items():
            if v > max_value:
                max_value = v
        return max_length - max_value