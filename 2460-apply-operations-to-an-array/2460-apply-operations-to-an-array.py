class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        
        print(nums)
        temp = []
        
        for i in nums:
            if i == 0:
                temp.append(i)
        
        
        zero_count = nums.count(0)
        
        for i in range(zero_count):
            nums.remove(0)
        
        nums.extend(temp)
        
        return nums