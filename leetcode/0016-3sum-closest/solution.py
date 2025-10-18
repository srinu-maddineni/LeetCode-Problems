class Solution(object):
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        curr = 0
        close = float('inf')
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left < right:
                curr = nums[i]+nums[left]+nums[right]
                if abs(curr - target) < abs(close - target):
                    close = curr
                if curr <target:
                    left+=1
                elif curr > target:
                    right-=1
                elif curr == target:
                    return curr
        return close





            


        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
