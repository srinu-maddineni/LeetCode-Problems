class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        while i<len(nums):
            m = 1
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    m+=1
                else: break
            if m >2:
                print('k')
                for k in range(i+m-1,i+1,-1):
                    nums.pop(k)
            i+=min(m,2)
        return len(nums)

        