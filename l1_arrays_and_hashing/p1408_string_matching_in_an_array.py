# 1408. String Matching in an Array
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result_list = set()
        for i in range(0,len(words)):
            for j in range(i+1,len(words)):
                if len(words[i]) != len(words[j]):
                    if (words[i] in words[j]):
                        result_list.add(words[i])
                    elif(words[j] in words[i]):
                        result_list.add(words[j])
        return list(result_list)