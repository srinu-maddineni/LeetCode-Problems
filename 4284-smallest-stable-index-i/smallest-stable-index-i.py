class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mx = 0
        index = float('inf')
        for i in range(len(nums)):
            mx = max(mx,nums[i])
            mn = float('inf')
            for j in range(i,len(nums)):
                mn = min(mn,nums[j])
            d = mx - mn 
            if d<=k:
                return i
        return -1
        