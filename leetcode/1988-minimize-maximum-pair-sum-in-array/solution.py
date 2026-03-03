class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        arr =[]
        i = 0
        j = len(nums)-1
        while i<j:
            arr.append(nums[i]+nums[j])
            i+=1
            j-=1
        print(arr)
        return max(arr)
        
