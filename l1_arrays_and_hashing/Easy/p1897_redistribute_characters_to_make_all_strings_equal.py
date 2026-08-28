class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        char_dict = dict()
        for word in words:
            for char in word:
                char_dict[char] = char_dict.get(char, 0) + 1
        
        for k, v in char_dict.items():
            if v % len(words) != 0:
                return False
        return True