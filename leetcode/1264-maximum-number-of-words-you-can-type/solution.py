class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        k = text.split()
        p = 0
        for i in k:
            n =0 
            for m in brokenLetters:
                if m not in i:
                    n+=1
            if n == len(brokenLetters):
                p+=1
        return p
   
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        
