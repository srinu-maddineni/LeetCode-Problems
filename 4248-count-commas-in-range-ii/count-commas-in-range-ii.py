class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        ans = 0
        i=1
        while i<6:
            ans += max(0,n-10**(3*i)+1)
            i+=1
        return ans

        