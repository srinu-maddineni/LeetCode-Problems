class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if s == goal:
            return True
        for i in range(len(s)):
            if s[i:]+s[:i] == goal:
                return True
        return False
        