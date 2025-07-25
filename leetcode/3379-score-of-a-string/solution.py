class Solution(object):
    def scoreOfString(self, s):
        m = 0
        for i in range(1,len(s)):
            m +=abs(ord(s[i]) - ord(s[i-1]))
        
        return m


        """
        :type s: str
        :rtype: int
        """
        
