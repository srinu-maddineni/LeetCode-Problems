class Solution:
    def countBits(self, n: int) -> List[int]:
        if n ==0:
            return [0]
        if n ==1:
            return [0,1]
        dp =[0]*(n+1)
        print(dp)
        dp[1] =1
        dp[2] = 1
        if n ==2:
            return [0,1,1]
        l = 2 
        for i in range(3,n+1):
            if i == l*2:
                l = i
                dp[i] = 1
            else:
                dp[i] = dp[l]+dp[i-l]
        return dp