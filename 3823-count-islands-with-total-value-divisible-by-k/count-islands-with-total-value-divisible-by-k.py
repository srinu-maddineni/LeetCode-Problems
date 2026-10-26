class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        res = 0
        n,m = len(grid),len(grid[0])
        def dfs(i,j):
            if i<0 or i>=n or j<0 or j>=m :
                return 0
            
            if grid[i][j] ==0:
                return 0
            # s+=grid[i][j]
            # print(s)
            # grid[i][j] =0
            # a = dfs(i+1,j,s)
            # b = dfs(i-1,j,s)
            # c = dfs(i,j+1,s)
            # d = dfs(i,j-1,s)
            r = grid[i][j]
            grid[i][j] = 0
            return r+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] !=0:
                    s = dfs(i,j)
                    print(s)
                    if s%k ==0:
                        res+=1
        return res
            
            