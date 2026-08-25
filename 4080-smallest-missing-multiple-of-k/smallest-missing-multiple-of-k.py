class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = set(nums)
        print(s)
        i = 1
        while True:
            if i*k not in s:
                return i*k
            i+=1
