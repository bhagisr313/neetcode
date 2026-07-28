class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        result = []
        for query in queries:
            counter = 0
            for j in range(query[0], query[1]+1):
                if (words[j][0] in "aeiou") and (words[j][-1] in "aeiou"):
                    counter += 1
            result.append(counter)
        return result


#efficient solution
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        result = []
        prefix_array = []
        binary_array = []
        for word in words:
            if word[0] in "aeiou" and word[-1] in "aeiou":
                binary_array.append(1)
            else:
                binary_array.append(0)
        prefix_sum = 0
        for ele in binary_array:
            prefix_sum += ele
            prefix_array.append(prefix_sum)

        for query in queries:
            right = query[1]
            left = query[0]
            if left == 0:
                result.append(prefix_array[right])
            else:
                result.append(prefix_array[right] - prefix_array[left-1])
        return result
