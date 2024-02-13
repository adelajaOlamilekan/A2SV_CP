class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        result = (num-3)/3
        
        if result.is_integer():
            return [int(result), int(result+1), int(result+2)]