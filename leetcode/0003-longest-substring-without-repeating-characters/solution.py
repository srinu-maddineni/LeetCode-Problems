class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        k = []
        
        m = 0
        for i in range(len(s)):
            j = i+1
            c = 0
            k =""
            k+=s[i]
            while j < len(s) and s[j] not in k:
                k +=s[j] 
                c +=1
                j+=1
            print(k)
            m = max(m,c)
       
        return m+1
        """
        :type s: str
        :rtype: int
        """
        
