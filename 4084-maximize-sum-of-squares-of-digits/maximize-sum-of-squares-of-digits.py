class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        ans = []
        while len(ans)<num:
            curr = min(9,sum)
            sum-=curr
            ans.append(str(curr))
        if sum >0: return ''
        return ''.join(ans)