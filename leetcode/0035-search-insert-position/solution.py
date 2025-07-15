class Solution(object):
    def searchInsert(self, nums, target):
        
        n = len(nums)
        for i in range(n):
            if nums[i] == target or nums[i] > target:
                return i
        return i+1
            
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
