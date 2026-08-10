class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = 0
        my_dict = dict()
        for i in range(0,len(text)):
            if text[i] not in my_dict:
                my_dict[text[i]] = 1
            else:
                my_dict[text[i]] += 1
        keys_exhausted = False
        while not keys_exhausted:
            for i in 'balloon':
                if i in my_dict:
                    if my_dict[i] > 0:
                        my_dict[i] -= 1
                    else:
                        return counter
                else:
                    return 0
            counter += 1
        return counter
                
