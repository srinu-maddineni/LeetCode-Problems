class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        k = set(nums)
        return len(nums) != len(k)
        
