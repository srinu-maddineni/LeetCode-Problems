class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = nums[0]
        sm = 0
        for i in range(len(nums)):
            sm+=nums[i]
            mx = max(mx,sm)
            if sm<0:
                sm = 0
            
        return mx
        