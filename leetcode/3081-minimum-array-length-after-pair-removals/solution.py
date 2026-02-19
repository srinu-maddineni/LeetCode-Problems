class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        # arr1 = nums[:len(nums)//2]
        # arr2 = nums[len(nums)//2:]
        # print(arr1,arr2)
        # i=0
        # j=0
        # k=0
        # while i<len(arr1) and j<len(arr2):
        #     if len(arr1) ==0 or len(arr2) ==0:
        #         break
        #     if arr1[i]<arr2[j]:
        #         k+=1
        #         j+=1
        #         i+=1
        #     else:
        #         j+=1

        # return len(nums)-2*k
        n = len(nums)
        freq = Counter(nums)
        mx = max(freq.values())
        if mx>n//2:
            return mx*2 - n
        else:
            return n%2
        
