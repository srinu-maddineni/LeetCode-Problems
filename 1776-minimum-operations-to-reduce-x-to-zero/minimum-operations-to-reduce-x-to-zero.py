class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        op = float('inf')
        n = len(nums)
        if nums[0] ==x or nums[n-1] ==x:
            return 1
        
        prev =[nums[0]]
        suff={}
        
        s =nums[n-1]
        suff[s] = 1
        for i in range(1,n):
            s1=prev[i-1]+nums[i]
            if s1==x:
                op = min(op,i+1)
            prev.append(s1)
            s+=nums[n-i-1]

            if s ==x:
                op = min(op,i+1)
            suff[s] = i+1
        if prev[n-1] <x:
            return -1
        for i in range(n):
            t = x-prev[i]
            if suff.get(t):
                op = min(op,i+1+suff[t])
        if op ==float('inf'):return -1
        return op

       
