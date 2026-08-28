class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre = 0
        # suff = 0
        # i = 0
        # j=len(nums)-1
        # while i<j:
        #     pre+=nums[i]
        #     suff+=nums[j]
        #     if pre == suff:
        #         return i+1
        #     if pre <suff: i+=1
        #     if suff <pre: j-=1
        # return -1
        s = sum(nums)
        l = 0
        for i in range(len(nums)):
            r = s-l-nums[i]
            if r==l:
                return i
            l+=nums[i]
        return -1