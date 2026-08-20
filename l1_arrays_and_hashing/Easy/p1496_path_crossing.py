class Solution:
    def isPathCrossing(self, path: str) -> bool:
        direction_set = set()
        coordinates = (0,0)
        direction_set.add(coordinates)
        for dir in path:
            new_tup = (0,0)
            if dir == "N":
                new_tup = (coordinates[0], coordinates[1] + 1)
            elif dir == "S":
                new_tup = (coordinates[0], coordinates[1] - 1)
            elif dir == "E":
                new_tup = (coordinates[0] + 1, coordinates[1])
            else:
                new_tup = (coordinates[0] - 1, coordinates[1])
            coordinates = new_tup
            if coordinates not in direction_set:
                direction_set.add(coordinates)
            else:
                return True
        return False