class Solution(object):
    def divide(self, dividend, divisor):
        # print(dividend/-(divisor))
        if dividend<0 and divisor<0:
            if dividend/divisor > ((2**31) -1):
                return dividend/divisor -1
            else:
                return dividend/divisor
        elif divisor<0:
            return -(dividend/(-divisor))
        elif dividend<0:
            return -(-dividend/divisor)
        else:
            return dividend/divisor

        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
