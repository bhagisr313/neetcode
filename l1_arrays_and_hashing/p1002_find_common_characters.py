class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        my_list_dict = []
        result = []
        for word in words:
            word_count = dict()
            for char in word:
                word_count[char] = word_count.get(char,0) + 1
            my_list_dict.append(word_count)
        for i in range(0,len(my_list_dict)):
            
