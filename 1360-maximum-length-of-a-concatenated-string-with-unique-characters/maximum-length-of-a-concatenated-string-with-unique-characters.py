class Solution:
    def maxLength(self, arr: list[str]) -> int:
        m = 0
        n = len(arr)
        ans = 0
        

        def back(i,r):
            nonlocal ans
            if len(r) != len(set(r)): 
                return
            ans = max(ans,len(r))
            for j in range(i,n):
                back(j+1,r+arr[j])
        back(0,'')
        return ans