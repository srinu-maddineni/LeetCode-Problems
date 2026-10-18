class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        arr = [0]*26
        for i in range(len(s)):
            arr[ord(s[i])-97]+=cost[i]
        print(arr)
        arr.sort()
        res = 0
        mx=0
        for i in range(26):
            mx = max(mx,arr[i])
            res+=arr[i]
        return res-mx