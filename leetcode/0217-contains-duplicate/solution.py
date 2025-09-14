class Solution(object):
    def containsDuplicate(self, nums):
        k = set(nums)
        if len(nums) == len(k):
            return False
        else:
            return True
        """
        :type nums: List[int]
        :rtype: bool
        """
        
