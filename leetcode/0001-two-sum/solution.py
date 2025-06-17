class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hasmap={}
        for i,n in enumerate(nums):
            inverter = target-n
            if inverter in hasmap:
                return[hasmap[inverter],i]
            hasmap[n] = i
