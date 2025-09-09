class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        c = 10**9 + 7
        k =[0] *(n+1)
        k[1] = 1
        for i in range(1,n+1):
            for j in range(i+delay , min(i+forget , n+1)):
                k[j] = (k[j]+k[i])%c
        r = 0
        for i in range(n-forget+1 , n+1):
            r = (r+k[i])%c
        return r


            
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        
