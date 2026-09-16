class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        # dp = [[-1]*n for _ in range(n)]

        # def help(i,j):
        #     if i == n:
        #         return 0
        #     if  j>=n or j<0:
        #         return float('inf')
        #     if dp[i][j] != -1: return dp[i][j]

        #     dp [i][j] = matrix[i][j]+min(help(i+1,j-1),help(i+1,j),help(i+1,j+1))
        #     return dp[i][j]
        # ans = float('inf')

        # for i in range(n):
        #     ans = min(ans,help(0,i))
        # return ans

        dp = [r[:] for r in matrix]


        for i in range(n-2,-1,-1):
            for j in range(n):
                l = dp[i+1][j-1] if j>0 else float('inf')
                m = dp[i+1][j] 
                r = dp[i+1][j+1] if j<n-1 else float('inf')
                dp[i][j] = matrix[i][j]+ min(l,m,r)
        return min(dp[0])