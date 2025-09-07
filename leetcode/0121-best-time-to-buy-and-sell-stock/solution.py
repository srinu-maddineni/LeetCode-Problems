class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        for i in prices:
            if min_price > i:
                min_price = i
            profit = i - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit


        """
        :type prices: List[int]
        :rtype: int
        """
        
