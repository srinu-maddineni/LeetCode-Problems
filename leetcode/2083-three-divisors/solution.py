class Solution:
    def isThree(self, n: int) -> bool:
        def prime(n):
            print(n)
            if n <2:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i == 0:
                    return False
            return True
        r = int(n**0.5)
        if r*r != n:
            return False
        return prime(int(n**0.5))


        
