class Solution(object):
    def sortVowels(self, s):
        i = 0
        j = len(s)
        k = []
        v = ['a','e','i','o','u','A','E','I','O','U']
        for i in s:
            if i in v:
                k.append(ord(i))
        
        k.sort()
        j = 0
        s_list = list(s)
        for i in range(len(s)):
            if s[i] in v:
                r = k[j]
                s_list[i] = chr(r)
                j+=1
        return "".join(s_list)


        
       

            
        """
        :type s: str
        :rtype: str
        """
        
