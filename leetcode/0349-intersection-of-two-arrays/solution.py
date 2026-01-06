class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h1 = {}
        r = set()
        for i in nums1:
            if i in h1:
                h1[i] +=1
            else:
                h1[i] = 1
        for i in nums2:
            if i in h1:
                r.add(i)
        return list(r)

        
