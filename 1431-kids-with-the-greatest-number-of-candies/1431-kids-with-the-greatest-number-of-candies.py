class Solution:
    
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        max_value = max(candies)
        result = [False]*len(candies)
        
        
        for index, val in enumerate(candies):
            val += extraCandies
            if val >= max_value:
                result[index] = True
        return result
            
            
            