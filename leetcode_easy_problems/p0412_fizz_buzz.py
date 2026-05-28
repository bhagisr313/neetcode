class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                i = "FizzBuzz"
            elif i % 3 == 0:
                i = "Fizz"
            elif i % 5 == 0:
                i = "Buzz"
            else:
                i = str(i)
            res.append(i)
        return res