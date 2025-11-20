class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        arr = [[0]*n for _ in range(n)]
        left =0
        right = n-1
        top,down=0,n-1
        j = 1
        while left<=right and top<=down:
            for i in range(left,right+1):
                arr[top][i] = j
                j+=1
            top+=1
            for i in range(top,down+1):
                arr[i][right] = j
                j+=1
            right-=1
            if left<=right:
                for i in range(right,left-1,-1):
                    arr[down][i] =j
                    j+=1
                down-=1
            if top<=down:
                for i in range(down,top-1,-1):
                    arr[i][left]=j
                    j+=1
                left+=1
        return arr

        
