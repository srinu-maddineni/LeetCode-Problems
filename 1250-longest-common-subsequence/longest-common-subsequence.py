class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1]*len(text2) for _ in range(len(text1))]
        def help(i,j,s,s1,dp):
            if i<0 or j<0:
                return 0
            if dp[i][j] != -1: return dp[i][j]
            if s[i] == s1[j]:
                dp[i][j] = 1+help(i-1,j-1,s,s1,dp)
                return dp[i][j]
            dp[i][j]=max(help(i-1,j,s,s1,dp),help(i,j-1,s,s1,dp))
            return dp[i][j]
        return help(len(text1)-1,len(text2)-1,text1,text2,dp)
        