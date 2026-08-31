class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        c= Counter(s)
        r = sorted(c.items(),key=lambda x:x[1],reverse=True)
        print(c)
        s =''
        for (i,j) in r:
            s = s+(j*i)
        return s
        
