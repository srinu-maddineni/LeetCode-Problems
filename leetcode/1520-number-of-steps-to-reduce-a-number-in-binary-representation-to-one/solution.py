class Solution:
    def numSteps(self, s: str) -> int:
        n = int(s,2)
        c =0
        def OddEven(num):
            if num%2 == 0:
                return True
            else:
                return False
        while True:
            if n == 1:
                return c
            if OddEven(n):
                n //=2
                c+=1
            else:
                n+=1
                c+=1
            


        
