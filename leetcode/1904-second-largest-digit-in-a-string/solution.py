class Solution(object):
    def secondHighest(self, s):
        a = []
        for i in range(len(s)):
            if s[i:i+1].isdigit():
                a.append(s[i:i+1])
        f = -1
        sec = -1
        for i in range(len(a)):
            if f<a[i]:
                sec = f
                f = a[i]
                
            if sec < a[i] and f != a[i]:
                sec = a[i]
        # if sec == f:
        #     return -1
        return int(sec)
        """
        :type s: str
        :rtype: int
        """
        
