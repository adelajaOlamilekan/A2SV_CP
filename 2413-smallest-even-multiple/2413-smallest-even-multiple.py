class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2 == False:
            return n
        else:
            return n*2
        