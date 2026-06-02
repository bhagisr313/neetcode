# 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        is_valid = True
        bracket_mapping = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }
        for i in s:
            if i in bracket_mapping.values():
                stack.append(i)
            else:
                if len(stack) > 0:
                    popped = stack.pop()
                    if popped != bracket_mapping[i]:
                        is_valid = False
                        break
                else:
                    is_valid = False
                    break
        if len(stack) > 0:
            is_valid = False
        return is_valid