class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        INF = float('inf')
        best = [INF]* (len(arr)+1)
        l = 0
        s =0
        ans=INF
        for i in range(len(arr)):
            s+=arr[i]
            while s>target:
                s-=arr[l]
                l+=1
            best[i + 1] = best[i]
            if s==target:
                r = i-l+1
                if best[l] != INF:
                    ans = min(ans, r + best[l])

                best[i + 1] = min(best[i + 1], r)
        

        return -1 if ans == INF else ans

        
