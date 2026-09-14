class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        x1 = rec1[2]
        y1 = rec1[3]
        x2 = rec2[0]
        y2 = rec2[1]

        x3 = rec1[0]
        y3 = rec1[1]
        x4=rec2[2]
        y4=rec2[3]

        if x1>x2 and y1>y2 and x4>x3 and y4>y3 :
            return True
        return False