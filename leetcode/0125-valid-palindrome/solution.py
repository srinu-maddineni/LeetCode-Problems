class Solution(object):
    def isPalindrome(self, s):
        k = ''
        
        for sr in s.lower():
            if sr.isalnum():
                k+=sr
        return k == k[::-1]

        """
        :type s: str
        :rtype: bool
        """
        
