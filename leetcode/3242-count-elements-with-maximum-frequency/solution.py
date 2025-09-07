from collections import Counter
class Solution(object):
    def maxFrequencyElements(self, nums):
        k = {}
        for i in nums:
            if i not in k:
                k[i] = 1
            else:
                k[i] +=1
        print(k)
        m = 0
        for  c in k.values():
            if c > m:
                m = c
        r = []
        for v,c in k.items():
            if c == m:
                r.append(v)
        return len(r) * m


        """
        :type nums: List[int]
        :rtype: int
        """
        
