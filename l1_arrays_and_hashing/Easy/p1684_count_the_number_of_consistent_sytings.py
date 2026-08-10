class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter = 0
        for word in words:
            char_found = True
            for char in word: 
                if char not in allowed:
                    char_found = False
                    break
            if char_found:
                counter += 1
        return counter