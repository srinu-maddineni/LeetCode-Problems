class Solution(object):
    def searchRange(self, nums, target):
        # if len(nums) ==1 and target ==nums[0]:
        #     return [0,0]
        l = 0
        r = len(nums)-1
        num = []
        while l<=r:
            if nums[l] == target and nums[r] == target:
                return [l,r]
            elif nums[l] == target and nums[r] != target:
                num.append(l)
                r-=1
                continue
            elif nums[r] == target and nums[l] != target:
                num.append(r)
                l+=1
                continue
            else:
                l+=1
                r-=1
        if len(num) != 0:
            return num.sort()
        else:
            return [-1,-1]
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
