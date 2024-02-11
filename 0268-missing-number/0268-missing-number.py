class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        len_nums = len(nums)
        nums_sum = sum(nums)
        actual_sum = (len_nums * (len_nums+1)) // 2
        
        return int(actual_sum - nums_sum)
        