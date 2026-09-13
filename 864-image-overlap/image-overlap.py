class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        ans = 0
        pos = []
        pos1 = []
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j] == 1:
                    pos.append((i,j))
                if img2[i][j] ==1:
                    pos1.append((i,j))


        c = {}

        for x1,y1 in pos:
            for x2,y2 in pos1:
                s = (x2-x1,y2-y1)
                c[s] = c.get(s,0)+1
                ans = max(ans,c[s])
        return ans
