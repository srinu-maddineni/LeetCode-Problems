class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        n=len(grid)
        m = len(grid[0])
        dp = [[[-1] * (n + m) for _ in range(m)] for _ in range(n)]

        def help(i,j,stk):
            if i<0 or j<0 :
                return False
            o = stk
            if dp[i][j][o] != -1:
                return dp[i][j][o] ==1
            if grid[i][j] == '(':
                if stk ==0:
                    return False
                stk-=1

            else:
                stk+=1

            if i==0 and j==0:
                return stk ==0
            

            ans = help(i-1,j,stk) or help(i,j-1,stk)
            dp[i][j][o] = 1 if ans else 0
            return ans
        
        return help(n-1,m-1,0)