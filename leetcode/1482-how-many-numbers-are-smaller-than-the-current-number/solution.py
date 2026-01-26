class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # nums.sort()
        k = []
        for i in range(len(nums)):
            m = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:

                    m+=1
            k.append(m)
        return k

        
