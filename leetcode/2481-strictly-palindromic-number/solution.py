class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def basic(n,base):
            if n ==0:return 0
            temp = []
            while n>0:
                temp.append(str(n%base))
                n//=base
            return "".join(reversed(temp))
        for i in range(2,n-1):
            k = basic(n,i)
            print(k)
            if k != k[::-1]:
                return False
        return True

        
