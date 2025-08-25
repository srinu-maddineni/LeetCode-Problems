class Solution(object):
    def firstMissingPositive(self, nums):
        n = set(nums)
        for i in range(1,len(n)+2):
            if i not  in n:
                return i
        # return len(nums)+1
        """
        :type nums: List[int]
        :rtype: int
        """
        
