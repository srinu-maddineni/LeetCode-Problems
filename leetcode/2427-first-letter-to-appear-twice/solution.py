class Solution(object):
    def repeatedCharacter(self, s):
        k = []
        for i in s:
            if i in k:
                return i
            else:
                k.append(i) 
        """
        :type s: str
        :rtype: str
        """
        
