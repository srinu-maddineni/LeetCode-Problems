class Solution(object):
    def lengthOfLastWord(self, s):
        n = len(s)
        i = n-1
       
        while s[i] ==' ': i-=1
        print(i)
        count = 0
        for i in range(i+1):
            if s[i] != " ":
                count +=1
            else:
                count=0
        return count
        
        """
        :type s: str
        :rtype: int
        """
        
