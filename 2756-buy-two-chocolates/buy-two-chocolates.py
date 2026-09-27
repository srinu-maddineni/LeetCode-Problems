class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        f = float('inf')
        s = float('inf')
        for i in range(len(prices)):
            if prices[i]<f:
                s = f
                f = prices[i]
            elif prices[i]<s:
                s = prices[i]
        if f+s<=money:
            return money - (f+s)
        return money