class Solution:
    def reverse(self, x: int) -> int:
        
        if x==0:
            return 0
        if x >0:
            x = str(x)[::-1]
            if int(x) >= 2147483647:
                return 0
            return int(x)
        else:
            n = str(x)[1:]
            n = int('-'+n[::-1])
            print(n)
            if n <= -2147483648:
                return 0
            return n

