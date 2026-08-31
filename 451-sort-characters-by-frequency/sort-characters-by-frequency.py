class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        c= Counter(s)
        # r = sorted(c.items(),key=lambda x:x[1],reverse=True)
        
        s =''
        for i,j in c.most_common():
            s = s+(j*i)
        return s
        
