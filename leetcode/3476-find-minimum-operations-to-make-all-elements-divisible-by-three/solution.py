class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c = 0
        for i in nums:
            c += min(i%3,3-(i%3))
        return c

        
