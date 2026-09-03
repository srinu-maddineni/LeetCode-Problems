class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:

        small = False
        big = False
        mn = float('inf')
        for i in range(len(nums1)):
            if nums1[i] %2 !=0:
                small = True
            else:
                big = True
            mn = min(mn,nums1[i])

        if not small  or not big:
            return True
        
        return mn % 2 !=0

        