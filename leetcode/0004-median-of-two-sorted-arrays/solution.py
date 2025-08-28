class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
         k = sorted(nums1 + nums2)
         print(len(k))
         if len(k) <= 1:
            return k[0]

         if len(k) %2 != 0:
            return float(k[(len(k)) // 2])
         else:
            # print(k[(len(k)//2) -1])
            r = (k[(len(k)//2)-1] + k[(len(k) // 2 )])
            # print(r)
            if r <= 0:
                return 0
            else:

                return float(r/ 2)

        
