class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        k = len(nums)//2
        arr1 = nums[:k]
        arr2 = nums[k:]
        i = 0
        j = 0
        sol = 0
        while i<len(arr1) and j < len(arr2):
            if arr1[i]*2 <= arr2[j]:
                sol+=2
                i+=1
                j+=1
            else:
                j+=1
        return sol
                

        
