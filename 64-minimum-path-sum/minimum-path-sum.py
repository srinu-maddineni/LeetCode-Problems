class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        dp = [[-1]*len(grid[0]) for _ in range(len(grid))]
        # def help(i,j):
        #     if i<0 or j<0: return float('inf')
        #     if i==0 and j ==0:return grid[0][0]
        #     if dp[i][j] != -1:return dp[i][j]
        #     u = grid[i][j]+help(i-1,j)
        #     d = grid[i][j]+help(i,j-1)
        #     dp[i][j] = min(u,d)
        #     return dp[i][j]
        
        # return help(len(grid)-1,len(grid[0])-1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0 and j==0:
                    dp[0][0] = grid[0][0] 
                    continue
                u = float('inf')
                l = float('inf')
                if i>0:u=grid[i][j]+dp[i-1][j]
                if j>0:l=grid[i][j]+dp[i][j-1]
                dp[i][j] = min(u,l)
        return dp[len(grid)-1][len(grid[0])-1]