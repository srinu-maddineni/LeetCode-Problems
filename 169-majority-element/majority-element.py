class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        f = {}
        for i in nums:
            f[i] = f.get(i,0)+1
        print(f)
        m = 0
        ans = 0
        for i,j in f.items():
            if j>m:
                ans = i
                m = j
        return ans
        