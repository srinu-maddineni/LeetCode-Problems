class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k%n
        if n<= 0 or k <1 :
            return 
        
        
        
        print(nums[-k:]+nums[:n-k])
        nums[:]=nums[-k:]+nums[:n-k]
        return nums
        """
        Do not return anything, modify nums in-place instead.
        """
        
