class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def prime(n):
            # n = int(n)
            if n < 2:
                return False
            for i in range(2,int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True
        c = 0
        for i in range(left,right+1):
            k = bin(i)[2:]
            r= Counter(k)
            if prime(r["1"]):
                c+=1
        return c

        
