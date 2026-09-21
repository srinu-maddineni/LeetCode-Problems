class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0]*k
        dp = [0]*k
        for i in nums:
            rem = [0]*k
            rem[i%k]+=1
            for j in range(k):
                if dp[j]:
                    nr = (j*i)%k
                    rem[nr]+=dp[j]
            for r in range(k):
                ans[r] += rem[r]
            dp = rem      
        return ans
