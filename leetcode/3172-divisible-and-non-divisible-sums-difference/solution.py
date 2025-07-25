class Solution(object):
    def differenceOfSums(self, n, m):
        k = (n*(n+1))/2
        j =0
        for i in range(n+1):
            if i%m == 0:
                j+=i
        print(k -(2*j))
        return k-(2*j)
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        
