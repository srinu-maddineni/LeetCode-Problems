class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        num = []
        i =0

        while i <len(nums)-3:
            if i>0 and nums[i] == nums[i-1]:
                i+=1
                continue
            j = i+1
            while j <len(nums)-2:
                if j>i+1 and nums[j] == nums[j-1]:
                    j+=1
                    continue
                left = j+1
                right = len(nums)-1
                t = nums[i]+nums[j]
                while left<right:
                    r = nums[left]+nums[right]
                    if target == r+t:
                        num.append([nums[i],nums[left],nums[right],nums[j]])
                        left+=1
                        right-=1

                        while left<right and nums[left] == nums[left-1]:
                            left+=1
                        while left<right and nums[right] == nums[right+1]:
                            right-=1
                    elif r+t < target:
                        left+=1
                    else:
                        right-=1
                j+=1
            i+=1
        return num

            
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
