class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink =numBottles
        emty = numBottles
        while emty>=numExchange:
            emty-=numExchange
            drink+=1
            emty+=1
        
        return drink
        
