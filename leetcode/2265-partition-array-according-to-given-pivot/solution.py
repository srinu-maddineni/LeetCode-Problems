class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        g = []
        l = []
        e = []
        for i in nums:
            if i < pivot:
                l.append(i)
            elif i>pivot:
                g.append(i)
            else:
                e.append(i)
        return l+e+g

        
