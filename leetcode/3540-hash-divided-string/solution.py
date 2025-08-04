class Solution(object):
    def stringHash(self, s, k):
        r = ''
        for i in range(0,len(s),k):
            s1 = s[i:i+k]
            print(s1)
            n = 0
            for j in s1:
                n += (ord(j)-97)
            r += chr((n%26)+97)
            print(r)
        return r

        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
