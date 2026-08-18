class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """


        m = Counter(nums)
        n = len(nums)-1
        r = 0
        if k == 1:
            res = 0
            for i in m:
                if m[i] ==1 and i > res:
                    res = i
            if res == 0: return -1
            return res

        elif k == n+1:
            return max(nums)

        

        elif m[nums[n]] == 1:
            r = nums[n]
            if nums[n]>nums[0]:
                return r
            elif m[nums[0]] == 1:
                r = nums[0]
            return r
        elif m[nums[0]] ==1:
            return nums[0]
        return -1