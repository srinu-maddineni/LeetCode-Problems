class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid=[[0]*n for _ in range(m) ]
        for i,j in guards:
            grid[i][j] = 2

        for i,j in walls:
            grid[i][j] = 2


        for i,j in guards :
            for k in range(i+1,m):
                if grid[k][j] ==2: break
                grid[k][j] = 1
                    
            for r in range(j+1,n):
                if grid[i][r] == 2:break
                grid[i][r] = 1

            for a in range(i-1,-1,-1):
                if grid[a][j] == 2:break
                grid[a][j] = 1


            for b in range(j-1,-1,-1):
                if grid[i][b] == 2: break
                grid[i][b]=1
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count+=1
        return count

        
