class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c  = nums.count(1)
        if c>0:
            return len(nums)-c
        k = False
        ans = float('inf')
        for i in range(len(nums)):
            g= nums[i]
            for j in range(i,len(nums)):
                g = math.gcd(g,nums[j])
                if g == 1:
                    ans = min(ans,j-i)
                    break
        if ans == float('inf'):
            return -1
        return ans+len(nums)-1


        
