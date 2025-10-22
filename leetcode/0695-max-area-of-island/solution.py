class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n , m = len(grid) , len(grid[0])
        k = 0
        def dfs(i,j):
            if i<0 or i>=n or j<0 or j>=m or grid[i][j] == 0:
                return 0
            grid[i][j]=0
            return 1 + dfs(i,j+1) + dfs(i+1,j) + dfs(i,j-1) + dfs(i-1,j)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    r = dfs(i,j)
                    k = max(k,r)
        return k
