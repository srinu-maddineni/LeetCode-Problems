class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []
        
        for i in range(m):
            s = []
            for j in range(n):
                if i ==0 :
                    s.append('.')
                elif j==n-1:
                    s.append('.')
                else:
                    s.append('#')
            grid.append(''.join(s))
        return grid