class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        arr = [26-i for i in range(26)]
        print(arr)
        for  i in range(len(s)):
            ans += arr[ord(s[i])-97] * (i+1)
        return ans
