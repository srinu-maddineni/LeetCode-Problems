class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        a= 0
        b = 0
        ans = []
        for i in range(len(seq)):
            if seq[i] == '(':
                if a<=b:
                    a+=1
                    ans.append(0)
                else:
                    b+=1
                    ans.append(1)
            else:
                if a<=b:
                    b-=1
                    ans.append(1)
                else:
                    a-=1
                    ans.append(0)
        return ans
