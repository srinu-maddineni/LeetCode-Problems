class Solution(object):
    def jump(self, nums):
        c = 0
        m = 0
        j = 0
        n = len(nums)
        if n == 0 or n == 1:
            return 0
        for i in range(n):
            m = max(m,i+nums[i])
            if m >= n-1:
                return j+1
            if c == i:
                j+=1
                c = m

        """
        :type nums: List[int]
        :rtype: int
        """
        
