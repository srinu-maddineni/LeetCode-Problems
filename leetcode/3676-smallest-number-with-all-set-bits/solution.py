class Solution(object):
    def smallestNumber(self, n):
        s = ''
        while n>0:
            if n/2 == 0:
                s+='0'
            else:
                s+='1'
            n = n/2
        r =0
        s=s[::-1]

        for i in range(len(s)):
            r+=2**i
        return r






        """
        :type n: int
        :rtype: int
        """
        
