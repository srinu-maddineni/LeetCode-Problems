class Solution(object):
    def getNoZeroIntegers(self, n):
        
        # a.append(1)
        # a.append(n-1)
        for i in range(1,n//2+1):
            b = n-i

            if '0' not in str(b) and '0' not in str(i) :
                return [i,b]


        
        """
        :type n: int
        :rtype: List[int]
        """
        
