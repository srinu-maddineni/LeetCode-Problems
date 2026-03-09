class Solution:
    def rotatedDigits(self, n: int) -> int:
        s = 0
        r= ['3','4','7']
        l =['2','5','6','9']
        for i in range(1,n+1):
            s1= str(i)
            c=0
            k = 0
            for j in s1:
                if j in r:
                    k+=1
                    break
                else:
                    if j in l:
                        c+=1
            if c >0 and k ==0:
                s+=1
        return s


        return s


