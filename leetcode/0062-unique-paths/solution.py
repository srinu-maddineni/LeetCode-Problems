class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr= [[0]*n for _ in range(m)]
        arr[0][0]=1
        for i in range(m):
            for j in range(n):
                if i == j ==0:
                    continue
                val=0
                if i>0:
                    val+=arr[i-1][j]
                if j>0:
                    val+=arr[i][j-1]
                arr[i][j]=val
        print(arr)
        return arr[m-1][n-1]

        
