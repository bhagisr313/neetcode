class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        my_dict = dict()

        for char in chars:
            my_dict[char] = my_dict.get(char,0)+1

        for word in words:
            letter_dict = dict()
            for ch in word:
                letter_dict[ch] = letter_dict.get(ch,0)+1
            word_found = True
            for k, v in letter_dict.items():
                if k in my_dict and v <= my_dict[k]:
                    continue
                else:
                    word_found = False
            if word_found:
                res += len(word)
        return res