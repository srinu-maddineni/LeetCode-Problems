class Solution:
    def minMoves(self, nums: list[int]) -> int:
        res = sum(nums) - min(nums)*len(nums)
        # for i in nums:
        #     if i ==0:
        #         continue
        #     res+=i-1
        return res