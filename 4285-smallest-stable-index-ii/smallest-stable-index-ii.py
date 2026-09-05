class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        print(nums[0])
        mx = 0
        pre = [0]*n
        print(pre)
        pre[0] = nums[0]
        suff = [float('inf')]*n 
        suff[n-1] = nums[n-1]
        for i in range(1,n):
            pre[i] = max(nums[i],pre[i-1])
            suff[n-i-1] = min(nums[n-i-1],suff[n-i])

        for i in range(n):
            if pre[i] - suff[i] <=k:
                return i 


        return -1

