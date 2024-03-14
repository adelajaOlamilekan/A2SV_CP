class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = int("".join(map(str, digits)))
        digits += 1
        
        result = []
        
        while digits/10 != 0:
            # ans = digits%10
            # print(ans)
            result.insert(0, digits%10)
            digits//=10
            
        return result
            