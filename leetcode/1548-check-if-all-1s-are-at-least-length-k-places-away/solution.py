class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k ==0:
            return True
        n  = len(nums)
        i = 0
        while i < n:
            if nums[i] == 1:
                if 1 in nums[i+1:i+k+1]:
                    return False
                else:
                    i+=k
            else:
                i+=1
        return True



        
