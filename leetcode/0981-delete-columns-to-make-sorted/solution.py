class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        k = 0
        for i in range(len(strs[0])):
            for j in range(len(strs)-1):
                print(strs[j][i],strs[j+1][i])
                if strs[j][i] > strs[j+1][i]:
                    k +=1
                    break
        return k

