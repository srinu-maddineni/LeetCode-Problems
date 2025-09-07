class Solution(object):
    def sumZero(self, n):
        a =[]
        if n % 2 == 0:
            for i in range(1,n//2+1):
                a.append(i)
                a.append(-1*i)
        else:
            a.append(0)
            for i in range(1,n//2+1):
                a.append(i)
                a.append(-1*i)
        return a


        """
        :type n: int
        :rtype: List[int]
        """
        
