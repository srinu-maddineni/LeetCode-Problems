class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo={}
        def back(i,j):
            if j == len(t):
                return 1
            if i == len(s): 
                return 0
            if (i,j) in memo: 
                return memo[(i,j)]
            ans=back(i+1,j)

            if s[i] == t[j]:
                ans+=back(i+1,j+1)
            memo[(i,j)] = ans
            return ans


        return back(0,0)


        