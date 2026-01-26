class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        j =[]
        for i in range(n):
            j.append(nums[i])
            j.append(nums[i+n])
            
            
        return j

        
