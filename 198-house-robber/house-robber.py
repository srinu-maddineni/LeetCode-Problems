class Solution:
    def rob(self, nums: List[int]) -> int:
        # max_sum =0
        # for i in range(len(nums)):
        #     s = 0
        #     for j in range(i,len(nums),2):
        #         s+=nums[j]
        #     if s>max_sum:
        #         max_sum = s
        # return max_sum
        n = len(nums)
        if  n==1:
            return nums[0]
        # dp =[0]*n
        # dp[0] = nums[0]
        # dp[1] = max(nums[1],nums[0])
        prev1 =0
        prev2=0
        for i in range(n):
            prev1,prev2 = max(nums[i]+prev2,prev1),prev1
        return prev1



            

        