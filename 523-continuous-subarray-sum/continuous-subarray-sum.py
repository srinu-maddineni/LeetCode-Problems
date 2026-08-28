class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        ar = []
        pre = 0
        m = {0:-1}
        for i in range(len(nums)):
            pre+=nums[i]
            r = pre%k
            if r in m:
                if i-m[r]>=2:
                    return True
            else:
                m[r] = i
        return False


        