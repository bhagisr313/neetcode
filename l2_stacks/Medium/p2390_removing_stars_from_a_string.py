class Solution:
    def removeStars(self, s: str) -> str:
        result_stack = []
        for char in s:
            if char != "*":
                result_stack.append(char)
            elif char == "*":
                result_stack.pop()
        return "".join(result_stack)