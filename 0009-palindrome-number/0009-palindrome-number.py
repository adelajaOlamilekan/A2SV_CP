class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        number_as_string = str(x)

        l = 0
        r = len(number_as_string)-1

        while l < r:
            if number_as_string[l] != number_as_string[r]:
                return False
            l+=1
            r-=1

        return True