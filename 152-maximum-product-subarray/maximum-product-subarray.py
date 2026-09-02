class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre = 1
        prev_max = float('-inf')
        n = len(nums)
        # for i in nums:
        #     pre *=i
        #     prev_max=max(prev_max,pre)
        #     if pre == 0:
        #         pre =1
        # print(prev_max)
        suff = 1
        suff_max = float('-inf')
        mx =float('-inf')
        for i in range(n):
            if suff ==0:
                suff =1
            if pre == 0:
                pre =1
            suff*=nums[n-i-1]
            pre *=nums[i] 
            mx= max(mx,max(suff,pre))

        return mx