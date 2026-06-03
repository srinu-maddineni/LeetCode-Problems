class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        a = 0
        for ch in set(s):
            left =s.find(ch)
            right=s.rfind(ch)
            if right - left>1:
                middle = set(s[left+1:right])
                a += len(middle)
        return a


