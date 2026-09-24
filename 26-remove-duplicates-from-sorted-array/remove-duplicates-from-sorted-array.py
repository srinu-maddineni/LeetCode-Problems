class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
    
        j = 1
        while j<len(nums):
            # print(i,nums[i],j,nums[j])
            if nums[j-1]==nums[j]:
                nums.pop(j)
            else:
                j+=1
        return 