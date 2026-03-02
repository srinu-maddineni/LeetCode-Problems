class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num %10 == 0 and num != 0:
            return False
        return  True
        # k = int(str(int(str(num)[::-1]))[::-1])
        # return k == num
        
