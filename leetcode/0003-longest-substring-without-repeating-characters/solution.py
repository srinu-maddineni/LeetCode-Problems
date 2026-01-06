class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r =0
        for i in range(len(s)):
            s1 =""
            for j in range(i,len(s)):
                if s[j] not in s1:
                    s1+=s[j]
                    if len(s1)>r:
                        r = len(s1)
                else:
                    break
        return r

