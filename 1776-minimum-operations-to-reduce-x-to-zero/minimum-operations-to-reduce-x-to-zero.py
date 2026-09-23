class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        # op = float('inf')
        # n = len(nums)
        # if nums[0] ==x or nums[n-1] ==x:
        #     return 1
        
        # prev =[nums[0]]
        # suff={}
        
        # s =nums[n-1]
        # suff[s] = 1
        # for i in range(1,n):
        #     s1=prev[i-1]+nums[i]
        #     if s1==x:
        #         op = min(op,i+1)
        #     prev.append(s1)
        #     s+=nums[n-i-1]

        #     if s ==x:
        #         op = min(op,i+1)
        #     suff[s] = i+1
        # if prev[n-1] <x:
        #     return -1
        # for i in range(n):
        #     t = x-prev[i]
        #     if suff.get(t):
        #         op = min(op,i+1+suff[t])
        # if op ==float('inf'):return -1
        # return op

        n = len(nums)
        t = sum(nums)-x
        if t<0: return -1
        if t==0:return n 
        print(t)
        l = 0
        
        j=0
        s =0
        for i in range(n):
            s += nums[i]
            while s>t:
                s-=nums[j]
                j+=1
            if s ==t:
                l=max(l,i-j+1)
        if l==0:return -1
        return n - l