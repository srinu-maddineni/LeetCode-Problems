class Solution(object):
    def plusOne(self, digits):
        m = 0
        d =digits[::-1]
        for i in range(len(d)):
            m += (d[i])*(10**i)
        m+=1
        k = []
        for i in str(m):
            k.append(int(i))
        return k

                
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
