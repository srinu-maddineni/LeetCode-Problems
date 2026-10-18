class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)
        m = 0
        j=0
        curr =0
        for i in range(n):
            if nums[i] ==0:
                curr +=1
            while curr >k:
                if nums[j] == 0:
                    curr-=1
                j+=1
                # curr = 0
            m = max(m,i-j+1)
        return m
