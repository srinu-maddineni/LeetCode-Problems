class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # s = set(nums)
        # print(s)
        # i = 1
        # while True:
        #     if i*k not in s:
        #         return i*k
        #     i+=1
        nums.sort()
        j =1
        for i in range(len(nums)):
            if j*k > nums[i]:
                continue
            elif j*k == nums[i]:
                j+=1
                continue
            else: return j*k
            j+=1
        return (j)*k
