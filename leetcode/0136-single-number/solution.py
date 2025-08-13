class Solution(object):
    def singleNumber(self, nums):
        r = 0
        for i in nums:
            r = r^i
        return r



        """
        :type nums: List[int]
        :rtype: int
        """
        
