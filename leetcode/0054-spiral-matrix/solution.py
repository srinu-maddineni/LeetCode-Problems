class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n,m = len(matrix),len(matrix[0])
        print(n,m)
        left , right = 0,m-1
        top,down = 0,n-1
        arr = []
        while left<=right and top<=down:
            for i in range(left,right+1):
                arr.append(matrix[top][i])
            top+=1
            
            for i in range(top,down+1):
                arr.append(matrix[i][right])
            right -=1
            
            if top <=down:
                for i in range(right,left-1,-1):
                    arr.append(matrix[down][i])
                down -=1
            if left<=right:
                for i in range(down,top-1,-1):
                    arr.append(matrix[i][left])
                left+=1
        print(arr)
        return arr

        
        
