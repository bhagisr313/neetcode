class Solution:
    def clearDigits(self, s: str) -> str:
        my_stack = []
        for i in s:
            if my_stack and i.isdigit():
                my_stack.pop()
            else:
                my_stack.append(i)
        return "".join(my_stack)