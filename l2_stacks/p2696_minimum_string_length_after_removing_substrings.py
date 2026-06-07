class Solution:
    def minLength(self, s: str) -> int:
        my_stack = []
        for i in s:
            if i == "B":
                if my_stack and my_stack[-1] == "A":
                    my_stack.pop()
                else:
                    my_stack.append(i)
            elif i == "D":
                if my_stack and my_stack[-1] == "C":
                    my_stack.pop()
                else:
                    my_stack.append(i)
            else:
                my_stack.append(i)
        return len(my_stack)
