class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre = 1
        prev_max = float('-inf')

        for i in nums:
            pre *=i
            prev_max=max(prev_max,pre)
            if pre == 0:
                pre =1
        print(prev_max)
        suff = 1
        suff_max = float('-inf')
        for i in range(len(nums)-1,-1,-1):
            suff*=nums[i]
            suff_max = max(suff_max,suff)
            if suff ==0:
                suff =1
        return max(suff_max,prev_max)