class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
    
        j = 1
        i=0
        while j<len(nums):
            # print(i,nums[i],j,nums[j])
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
            j+=1
            # else:
            #     j+=1
        return i+1