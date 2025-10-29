class Solution(object):
    def countAndSay(self, n):
        if n ==1:
            return '1'
        c='1'
        def count(num):
            s =''
            r =1
            for i in range(1,len(num)):
                if num[i-1] == num[i]:
                    r+=1
                else:
                    s+=str(r)+num[i-1] 
                    r = 1
            s+=str(r)+num[-1]
            return s

        for i in range(1,n):
            c=count(c)
        return c
            
            

        """
        :type n: int
        :rtype: str
        """
        
