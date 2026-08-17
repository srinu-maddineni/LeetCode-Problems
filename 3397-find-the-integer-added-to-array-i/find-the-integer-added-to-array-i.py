class Solution(object):
    def addedInteger(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        s1 = 0
        s2 = 0
        for i in range(len(nums1)):
            s1+=nums1[i]
            s2+=nums2[i]

        s3 = s2-s1
        return s3//len(nums1)