class Solution:
    def minCost(self, grid: list[list[int]]) -> int:

        n,m = len(grid),len(grid[0])
        dp = [[set() for _ in range(m)] for _ in range(n)]
        dp[0][0].add(grid[0][0])
        
        for i in range(1,m):
            x = next(iter(dp[0][i-1]))
            dp[0][i].add(x ^ grid[0][i])

        for j in range(1,n):
            x = next(iter(dp[j-1][0]))
            dp[j][0].add(x ^ grid[j][0])


        for i in range(1,n):
            for j in range(1,m):

                n1 = len(dp[i-1][j])
                n2 = len(dp[i][j-1])
                for i1 in dp[i-1][j]:
                    dp[i][j].add(i1^grid[i][j])
                for j1 in dp[i][j-1]:
                    dp[i][j].add(j1^grid[i][j])
        return min(dp[n-1][m-1])