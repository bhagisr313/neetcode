class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        result_stack = []
        i = 0

        for num in pushed:
            result_stack.append(num)

            while result_stack and result_stack[-1] == popped[i]: #will pop only when it matches the pop value, else keep on pushing the value
                result_stack.pop()
                i += 1

        return not result_stack