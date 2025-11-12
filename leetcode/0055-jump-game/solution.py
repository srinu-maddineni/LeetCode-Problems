class Solution(object):
    def canJump(self, nums):
        n = len(nums)
        t = n-1
        for i in range(n-1,-1,-1):
            m = nums[i]
            if i+m >= t:
                t = i
        return t==0

        """
        :type nums: List[int]
        :rtype: bool
        """
        
