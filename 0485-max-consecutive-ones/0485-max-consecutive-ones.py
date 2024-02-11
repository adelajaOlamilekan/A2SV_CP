class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_sum = 0
        temp = 0
        
        for i in nums:
            if i == 1:
                temp += i
                max_sum  = max(max_sum, temp)
            elif i == 0:
                temp = 0
        
        return max_sum
                
        