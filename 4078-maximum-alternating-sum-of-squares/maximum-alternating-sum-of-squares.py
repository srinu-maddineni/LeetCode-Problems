class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(len(nums)):
            if nums[i]<0:
                nums[i] *=-1
        
        nums.sort()
        k = n//2
        print(k)
        res = 0
        for i in range(k):
            res-= (nums[i]**2)
        for i in range(k,n):
            res+= (nums[i]**2)
        return res