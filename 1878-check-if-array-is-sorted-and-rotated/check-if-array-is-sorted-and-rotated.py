class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        j =0
        for i in range(len(nums)):
            if nums[i] > nums[(i+1)% len(nums)]:
                j+=1
        return j<=1