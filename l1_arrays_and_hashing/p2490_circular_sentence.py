class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        splited_array = sentence.split(" ")
        for i in range(0,len(splited_array)):
            j = i - 1
            if splited_array[i][0] != splited_array[j][-1]:
                return False
        return True