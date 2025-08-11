class Solution(object):
    def missingNumber(self, nums):
        # s = set(nums)
        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i
        n = len(nums)
        return n*(n+1)/2 - sum(nums)
        """
        :type nums: List[int]
        :rtype: int
        """
        
