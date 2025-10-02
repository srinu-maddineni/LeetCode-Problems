class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drink = 0 
        while numBottles>=numExchange:
            if numBottles >= numExchange:
                drink+=numExchange
                numBottles-=numExchange
                numExchange+=1
                numBottles+=1
                print(numBottles)
        return drink+numBottles
            

            
        
