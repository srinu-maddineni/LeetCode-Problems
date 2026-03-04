class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        c = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    if sum(mat[i]) == 1:
                        a =0
                        for k in range(n):
                            if k == i:
                                continue
                            if mat[k][j] == 1:
                                a+=1
                        if a==0:
                            c+=1
                            
        return c
        
