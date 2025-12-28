class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result =0
        for i in grid:
            h = len(i)-1
            l=0
            while l<=h:
                mid = (l+h)//2
                if i[mid]<0:
                    h=mid-1
                else:
                    l = mid+1
            result+=len(i)-l



        return result
        
        
